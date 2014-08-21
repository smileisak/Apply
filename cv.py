#!/usr/bin/python2
# -*- coding: iso-8859-1 -*-
#For attachements
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import sys
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
password = '***************' 
sender = 'your_fuckn_password'
recipient =  str(sys.argv[1])
subject = 'Test 2'
body = "fuck you all"

 
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sender
#msg['Reply-to'] = 'company@email.com'
msg['To'] = recipient
 
# That is what u see if dont have an email reader:
msg.preamble = 'Multipart massage.\n'

# This is the binary part(The Attachment):
part = MIMEApplication(open("Cv2Smile.pdf","rb").read())
part.add_header('Content-Disposition', 'attachment', filename="Cv2Smile.pdf")
msg.attach(part) 

# This is the textual part:
part = MIMEText(body)
msg.attach(part)
 


#Create Instance of SMTP Server
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)
 
session.sendmail(msg['From'], msg['To'], msg.as_string())
session.quit()
