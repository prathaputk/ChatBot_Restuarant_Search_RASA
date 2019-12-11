## short_path_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - utter_email_req
* affirm
    - email_form
    - form{"name":"email_form"} 
    - utter_goodbye

## complete_path_2
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - utter_email_req
* mail_id
    - email_form
    - form{"name":"email_form"}     
    - utter_goodbye

## short path 3
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - utter_email_req
* deny
    - utter_goodbye

## chit chat 1

* greet
    - utter_greet
* bot_challenge
    - utter_bot
* purpose
    - utter_purpose
* restaurant_search
    - restaurant_form
    - form{"name":"restaurant_form"}
    - utter_email_req
* affirm OR mail_id 
    - email_form
    - form{"name":"email_form"}
    
* goodbye
    - utter_goodbye

## chit chat 2

* greet
    - utter_greet
* feeling
    - utter_feeling
    - utter_ask_feeling
* mood_great
    - utter_celeb
* affirm
    - restaurant_form
    - form{"name":"restaurant_form"}
    - utter_email_req
* deny
    - utter_goodbye

## chit chat 3  

* greet
    - utter_greet
* feeling
    - utter_feeling
    - utter_ask_feeling
* mood_unhappy
    - utter_console
* affirm
    - restaurant_form
    - form{"name":"restaurant_form"}
    - utter_email_req
* affirm
    - email_form
    - form{"name":"email_form"}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* bot_challenge
    - utter_bot
* purpose
    - utter_purpose
* restaurant_search{"cuisine":"chinese"}
    - restaurant_form
    - form{"name":"restaurant_form"}
    - slot{"cuisine":"chinese"}
    - slot{"requested_slot":"location"}
* restaurant_search
    - action_default_fallback
* restaurant_search{"location":"chennai"}
    - restaurant_form
    - slot{"location":"chennai"}
    - slot{"requested_slot":"cost"}
* restaurant_search{"cost":"300 to 700"}
    - restaurant_form
    - utter_email_req
* mail_id{"email":"prathaputk@gmail.com"}
    - email_form
    - form{"name":"email_form"}
    - slot{"email":"prathaputk@gmail.com"}
    
* goodbye
    - utter_goodbye

## New Story 2

* greet
    - utter_greet
* feeling
    - utter_feeling
    - utter_ask_feeling
* mood_great
    - utter_celeb
* affirm
    - restaurant_form
* restaurant_search{"location":"mumbai"}
    - restaurant_form
    - slot{"location":"mumbai"}
    - slot{"requested_slot":"cuisine"}
* restaurant_search{"cuisine":"american"}
    - restaurant_form
    - slot{"cuisine":"american"}
* restaurant_search{"cost":"300 to 700"}
    - restaurant_form
    - utter_email_req
* deny
    - utter_goodbye


## New Story 3

* greet
    - utter_greet
* other_task
    - utter_unable
* restaurant_search
    - restaurant_form
    - form{"name":"restuarant_form"}
    - utter_email_req
* affirm
    - email_form
* goodbye
    - utter_goodbye    

## interactive_story_1
* greet
    - utter_greet
* purpose
    - utter_purpose
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "chennai"}
    - form: restaurant_form
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "cost"}
* form: restaurant_search{"cost": "less than 300"}
    - form: restaurant_form
    - slot{"cost": "less than 300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_email_req
* affirm
    - email_form
    - form{"name": "email_form"}
    - slot{"requested_slot": "email"}
* form: mail_id{"email": "prathaputk@gmail.com"}
    - form: email_form
    - slot{"email": "prathaputk@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* feeling
    - utter_feeling
    - utter_ask_feeling
* mood_great
    - utter_celeb
* affirm
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "bangalore"}
    - form: restaurant_form
    - slot{"location": "bangalore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "mexcian"}
    - form: restaurant_form
    - slot{"cuisine": null}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "american"}
    - form: restaurant_form
    - slot{"cuisine": "american"}
    - slot{"requested_slot": "cost"}
* form: restaurant_search{"cost": "more than 700"}
    - form: restaurant_form
    - slot{"cost": "more than 700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_email_req
* affirm
    - email_form
    - form{"name": "email_form"}
    - slot{"requested_slot": "email"}
* form: mail_id{"email": "prathaputk@gmail.com"}
    - form: email_form
    - slot{"email": "prathaputk@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye
