import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

class EmailSender():
    def __init__(self):
        
        json_file_path = 'config.json'
        with open(json_file_path, 'r') as file:
            self.configData = json.load(file)

    def send_email(self, subject, body, to_email):
        sender_email = self.configData["emailSender"]
        sender_password = self.configData["emailPassword"]

        # Set up the MIME
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject

        # Attach the body of the email
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server (Gmail in this case)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, to_email, message.as_string())

        recipient_email= self.configData["emailRecepient"]

        print("Email sent successfully!")

ES = EmailSender()

subject = "Sophisticated Test Email from Tyler"

body = """Hi,

Test email.

Thanks

"""

ES.send_email(subject, body, "tylertravisrhs@gmail.com")

   