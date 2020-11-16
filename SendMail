#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



expectedSongName='turn'

def mailnotification():
    print("emailing................")
    email = "" # the email where you sent the email
    password = "<ur password>"
    send_to_email = "<>" # for whom
    subject = "Gmail"
    message = "This is a test email sent by Python. Isn't that cool?!"

    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = send_to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print('Mail Sent')
