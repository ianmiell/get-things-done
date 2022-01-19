#!/usr/bin/python
import argparse
import sys
import smtplib
from email.mime.text import MIMEText

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--message', help='message',default='')
	args = parser.parse_args(sys.argv[1:])
	message = args.message
	key = open('mailkey','r').read().strip()
        if key == '' or key is None:
            print 'No Key'
        else:
	    send(key, message)

def send(key, message):
	print(message)
	msg = MIMEText(message.encode('ascii','ignore'))
	msg['Subject'] = "GTD alert: " + message
	msg['From']    = "gtd@mail.meirionconsulting.com"
	msg['To']      = "ian.miell@gmail.com"
	s = smtplib.SMTP('smtp.mailgun.org', 587)
	s.login('postmaster@mail.meirionconsulting.com', key)
	s.sendmail(msg['From'], msg['To'], msg.as_string())
	s.quit()
	print 'email sent'

main()
