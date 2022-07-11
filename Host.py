from email.message import EmailMessage
import smtplib
import ssl, requests
def Email(title='Subject',text='Message',your_mail='Sender Email'):
	message=EmailMessage()
	receiver=your_mail
	# sender=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/Mail/Email').text
	sender="emailtools2022@gmail.com"
	# password=requests.get('https://raw.githubusercontent.com/NongVu04/saver.github.io/main/Mail/password').text
	password="woxfmvqqsgzghshs"
	subject=title
	text=text
	message['From']=sender
	message['To']=receiver
	message['Subject']=subject
	message.set_content(text)
	context=ssl.create_default_context()
	with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
		server.login(sender,password)
		server.sendmail(sender,receiver,message.as_string())
Email("Hi Nong Hoang Vu", "Test 10:05AM", "servernv04@hotmail.com")
print("success")
