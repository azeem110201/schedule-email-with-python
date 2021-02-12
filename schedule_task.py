import schedule
import time
from datetime import datetime
import email, smtplib, ssl
from finance import ModelAnalysis
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from configparser import ConfigParser

file = "config.ini"
config = ConfigParser()
config.read(file)

def extract(ticker):
    ma = ModelAnalysis(ticker)
    ma.get_stock_name()

def job(args_):

    extract(args_[1])

    subject = "An email with attachment from Azeem"
    body = "This is an email with attachment sent from Azeem"
    sender_email = config['details']['email']
    receiver_email = args_[0]
    password = config['details']['password']

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    filename = "data.csv"  # In same directory as script

    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
    )    

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    
    try:
        os.remove("data.csv")
        print("data deleted")
    except Exception as e:
        print(e.message())    


    # server = smtplib.SMTP('smtp.gmail.com',587)
    # server.starttls()
    # server.login(sender_email, password)
    # print("Login successful")
    # server.sendmail(sender_email,receiver_email,message)
    # print("Email sent")

def get_email(email, ticker):
    # while True:
    #     schedule.every(20).seconds.do(job, email=email)
    #     schedule.run_pending()
    #     time.sleep(1)
    schedule.every(5).seconds.do(job, args_ = [email, ticker])
    while 1:
        n = schedule.idle_seconds()
        if n is None:
            break
        elif n > 0:
            time.sleep(0.5)
        schedule.run_pending()












# import schedule
# import time

# def job():
#     print('Hello')

# schedule.every(5).seconds.do(job)

# while 1:
#     n = schedule.idle_seconds()
#     if n is None:
#         # no more jobs
#         break
#     elif n > 0:
#         arr = [5,4,3,2,1]
#         arr.sort()
#         print(arr)
#         time.sleep(n)
#     schedule.run_pending()