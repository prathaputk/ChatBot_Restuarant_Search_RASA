# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from send_mail import app,mail
from flask_mail import Message
import re
import zomatopy
import json
import os



class RestaurantForm(FormAction):

	def name(self):
		return 'restaurant_form'


	@staticmethod
	def required_slots(tracker:Tracker)	:
		return ['location','cuisine','cost']

	def slot_mappings(self):
		
		return{'location': self.from_entity(entity='location'),'cuisine':self.from_entity(entity='cuisine'),'cost':self.from_entity(entity='cost') }

	@staticmethod
	def city_db():
		return ['bangalore','chennai','delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune', 'kochi', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore nagpur', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kottayam', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'perinthalmanna', 'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirur', 'tirupati', 'tirunelveli', 'tiruppur', 'tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'vellore', 'warangal', 'surat', 'visakhapatnam']

	def validate_location(self,value,dispatcher,tracker,domain):

		if value.lower() in self.city_db():
			return {'location':value}
		else:
			dispatcher.utter_template('utter_wrong_location',tracker)
			return {'location':None}	
		

	@staticmethod
	def cuisine_db():

		return ['american','south indian','chinese','italian','mexican']



	
	def validate_cuisine(self,value,dispatcher,tracker,domain):

		if value.lower() in self.cuisine_db():
			return{"cuisine":value}
		else:
			dispatcher.utter_template("utter_wrong_cuisine", tracker)
			return 	{"cuisine":None}	
		
	def submit(self,dispatcher,tracker,domain):
		cost_dict={'less than 300':"rest['restaurant']['average_cost_for_two'] <700",
		'300 to 700':"rest['restaurant']['average_cost_for_two'] <700 and rest['restaurant']['average_cost_for_two']>=300",
		'more than 700':"rest['restaurant']['average_cost_for_two'] >700"}
		cuisine_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		cuisine=tracker.get_slot('cuisine')
		cost=tracker.get_slot('cost')
		location=tracker.get_slot('location')
		cost_check=cost_dict[cost]

		config={ "user_key":"6c6e45db23a726185f67ab93e365b10b"}
		zomato = zomatopy.initialize_app(config)

		location_detail=zomato.get_location(location, 1)
		loc=json.loads(location_detail)
		lat=loc["location_suggestions"][0]["latitude"]
		lon=loc["location_suggestions"][0]["longitude"]

		fopen=open('log.txt','w')
		count=0
		start=0
		s=[]
		for _ in range(0,5):
			if count==10:
				break
			results=zomato.restaurant_search("", lat, lon, str(cuisine_dict.get(cuisine)), 20,'rating','desc',start)
			res=json.loads(results)
			for rest in res['restaurants']:
				if count==10:
					break
				if(eval(cost_check)):
					s.append(rest['restaurant']['name']+' in '+rest['restaurant']['location']['address']+' has been rated '+rest['restaurant']['user_rating']['aggregate_rating'])
					count+=1
			start+=20		
		if len(s):
			for i in range(0,min(5,len(s))):
				dispatcher.utter_message(s[i])
			for i in s:
				fopen.write(i+'\n')
					
		else:
			dispatcher.utter_message('Sorry,No matches found')
			fopen.write('Sorry,No match were found')

		fopen.close()
		return []	


class EmailForm(FormAction):

	def name(self):
		return 'email_form'

	@staticmethod
	def required_slots(tracker):
		return ['email']

	def get_slot():
		return {"email": self.from_entity(entity='email')}

	def validate_email(self,value,dispatcher,tracker,domain):
		if re.match(r'(^[\w.-]+@[\w-]+\.[\w.-]+$)',value):
			return {'email':value}
		else:
			dispatcher.utter_template("utter_wrong_email",tracker)	

		
		

	def submit(self,dispatcher,tracker,domain):

		os.environ['TICKET_LOCK_LFETIME']='85'
		recipient=tracker.get_slot('email')
		

		fopen=open('log.txt','r')

		body_text=fopen.read()

		fopen.close()
		
		with app.app_context():
			recipient=tracker.get_slot('email')
			msg = Message(subject="Here's a list of "+tracker.get_slot('cuisine')+" restaurant in "+tracker.get_slot('location'),
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[recipient], 
                      body=body_text)
			mail.send(msg)
		dispatcher.utter_template('utter_success',tracker)	

		return []

