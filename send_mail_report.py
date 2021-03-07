import email
import smtplib
import ssl # resource: https://realpython.com/python-send-email/
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


input_email = input("Insert your email and press enter: ")


# The method which automatically sends an email with HTML report in attachment
def send_mail(files=None, email=input_email):
    if files is None:
        files = ['reports/simple_test_report.html']
    subject = "Tests report"
    # body = input("Test description: ")
    body = 'Automated tests'
    sender_email = email
    # receiver_email = ['something@gmail.com', 'something@gmail.com', "something@gmail.com"
    #                   "something@gmail.comsomething@gmail.com', 'something@gmail.com']
    receiver_email = email

    password = input("Insert password")
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    for a_file in files:
        try:
            attachment = open(a_file, 'rb')
            file_name = os.path.basename(a_file)
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            part.add_header('Content-Disposition',
                            'attachment',
                            filename=file_name)
            encoders.encode_base64(part)
            message.attach(part)
        except:
            pass

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


# email_report_message -> string format
def send_mail_report(email_report_message):
    port = 465  # For SSL
    sender_email = input("Enter tester email and press enter button: ")
    receiver_email = sender_email
    password = input("Enter tester email password and press enter button: ")
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_report_message)  # Send email
        server.quit()