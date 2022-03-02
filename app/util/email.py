import os
import time
import requests
from dotenv import load_dotenv
from pathlib import Path
import smtplib, ssl

SERVER_URL = "https://icdpghana2.org/#/" #server to monitor
GRACE_PERIOD = 2 #check to higer for better telemetry eg..5
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
TO_EMAIL_ADDRESS = os.environ.get("TO_EMAIL_USER")


def build_simple_message():
    
    subject = 'YOUR SITE IS DOWN'
    body = 'Make sure the server restarted and it is backed up'
    #msg = f'Subject : {subject}\n\n{body}'
    # msg = "Subject: " + subject + "\n" + body
    msg = f"""
    Subject: Hi there, {subject}

    {body}
    
    """

    return msg


def send_email(message_type="simple"):
    
    # Create a secure SSL context
    # context = ssl.create_default_context()
        
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls() #secure the connection
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = build_simple_message()

        smtp.sendmail(EMAIL_ADDRESS, [TO_EMAIL_ADDRESS], msg)
        # close connection
        smtp.quit()
        smtp.close()
