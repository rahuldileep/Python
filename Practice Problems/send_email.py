#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

recipients = ['veda291092@gmail.com','iqrar.patel92@gmail.com']
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = str(sys.argv[1])
msg['From'] = 'rahuldileep@gmail.com'
#msg['Reply-to'] = 'iqrar.patel92@gmail.com'

msg.preamble = 'Multipart massage.\n'

part = MIMEText("Hi, please find the attached file")
msg.attach(part)

part = MIMEApplication(open(str(sys.argv[2]), "rb").read())
part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[2]))
msg.attach(part)
server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("rahuldileep@gmail.com", "newBEGINNING108")
server.sendmail(msg['From'], emaillist, msg.as_string())

