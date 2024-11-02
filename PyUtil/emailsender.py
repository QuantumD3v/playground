# email_utils.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Compose email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to Gmail's SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()  # Secure the connection
        smtp_server.login(sender_email, sender_password)  # Login

        # Send email
        smtp_server.send_message(message)
        print("Email sent successfully!")

        # Clean up
        smtp_server.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

