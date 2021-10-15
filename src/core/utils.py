from django.core.mail import EmailMessage

class Util:
	@staticmethod
	def send_email(data):
		
		email=EmailMessage(
			subject='Potential Client Form', body=data['email_body'], to=['bennyakambangwe@gmail.com','info@malingreats.org'])
		email.send()
