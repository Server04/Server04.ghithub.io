import imaplib
import email
receive="emailtools2022@gmail.com"
username =input('To: ')
Receive= f'(FROM "{receive}")'
app_password= "lnndxzoqmdzjviyg"
gmail_host= 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(gmail_host)
mail.login(username, app_password)
mail.select("INBOX")
_, selected_mails = mail.search(None, Receive)
print(f"Total Messages from {receive}:" , len(selected_mails[0].split()))

for num in selected_mails[0].split():
	_, data = mail.fetch(num , '(RFC822)')
	_, bytes_data = data[0]
	email_message = email.message_from_bytes(bytes_data)
	print("\n===========================================")
	print("Subject: ",email_message["subject"])
	print("To:", email_message["to"])
	print("From: ",email_message["from"])
	print("Date: ",email_message["date"])
	for part in email_message.walk():
		if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
			message = part.get_payload(decode=True)
			print("Message: \n", message.decode())
			print("==========================================\n")
			break
	for even in email_message.walk():
		if part.get_content_type()=="text/plain" or even.get_content_type()=="text/html":
			message = even.get_payload(decode=True)
			with open('list.txt', 'a+') as f:
				f.write(message.decode())
