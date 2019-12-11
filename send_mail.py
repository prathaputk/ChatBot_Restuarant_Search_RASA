from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'username',
	MAIL_PASSWORD = 'password'
	)
mail = Mail(app)

