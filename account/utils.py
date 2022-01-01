from  django.core.mail import send_mail
from Jmac.settings import EMAIL_HOST_USER
import time

def send_email(data):
    sender = EMAIL_HOST_USER
    reciever = data["to_email"]
    subject = data["email_subject"]
    body = data["email_body"]
    send_mail(subject, body, sender, [reciever], fail_silently=False)
    time.sleep(20)
       



        

