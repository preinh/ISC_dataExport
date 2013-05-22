# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os, re
import sys
import smtplib
 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'rede.geotectonica@gmail.com'
password = "redegeotec"
recipient = 'preinh@gmail.com, marlon.pirchiner@gmail.com'
subject = 'no_subject'
message = ''
 
def load_attachment(file):
    part = MIMEBase('application', "octet-stream")
    part.set_payload( open(file,"rb").read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    
    return part
    
#     # Read a file and encode it into base64 format
#     fo = open(filename, "rb")
#     filecontent = fo.read()
#     encodedcontent = base64.b64encode(filecontent)  # base64

 
def sendMail(filename):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = sender
 
    part = MIMEText('text', "plain")
    part.set_payload(message)
    msg.attach(part)

    msg.attach(load_attachment(filename))
 
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)
 
    session.sendmail(sender, recipient, msg.as_string())
    session.quit()
 
if __name__ == '__main__':
    sendMail()
        