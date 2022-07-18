import smtplib
import ssl
from email.message import EmailMessage



def send_mail(msg = "Sending Data", send_to = "michaeljalloh19@gmail.com", password = "nsswivqolbtvhmjo"):
    email_sender = 'watersolutions854@gmail.com'
    email_password = password
    email_receiver = send_to

    subject = 'Check out my new video!'
    body = msg

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
        print("Email Sent")
        return True

send_mail()