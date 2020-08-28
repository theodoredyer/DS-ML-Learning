import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)

    user = "theodore.austin.dyer@gmail.com"
    password = ""