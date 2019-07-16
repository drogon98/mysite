from celery.decorators import task
from django.core.mail import send_mail

@task()
def send_email(sender, message):
	# subject = "New customer alert!"
	subject = f"{ sender } have contacted you."
	send_mail(
    	subject,
    	message,
    	sender,
    	['infopixenweb@gmail.com',]
    	)