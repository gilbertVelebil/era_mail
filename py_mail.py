###########
# # CONSTANTS:
# from shared_constants import (
# 	INTERVAL_RUNNING,
# 	SMTP_ADDR, SMTP_PORT,
# 	CREDENTIALS_FILE,
# 	FROM, FROM_NM,
	# TO, TO_NM)
###########

import imaplib
import smtplib
import re
from email.mime.text import MIMEText
from email.header import Header
from utils import exceptTraceback

def getCredentials(file_nm):
	"""
	read and parse a text file
	return a list of [login name, password]
	"""
	try:
		with open(file_nm,'r') as f:
			content_split = f.read().split()
		return [content_split[0].strip(),content_split[1].strip()]
	except Exception as e:
		raise Exception(e)

def loginMail(imap_server,port,credentials):
	"""
	create an IMAP4_SSL object and log in using login name and password
	return the IMAP object
	"""
	try:
		imap_obj = imaplib.IMAP4_SSL(imap_server,port)
		resp = imap_obj.login(credentials[0],credentials[1])
		if resp[0] != 'OK':
			raise imaplib.IMAP4.error('Could not log in: ' + ", ".join([str(x) for x in resp[1]]))
		return imap_obj
	except imaplib.IMAP4.error as e:
		raise Exception(e)

def getEmails(imap_obj,mailbox,subj_text,move_emails=1):
	"""
	select mailbox off a logged-in email account and fetch emails based on the subject text
	return [Finally exceptions log, move emails error log, email bodies]
	where email bodies = [str_body1,'',str_body2,'',...] ('' for emails that could not be fetched)
	"""
	res = []
	res.append('') # Finally block exceptions (could not close mailbox and/or log out of the account)
	res.append('') # emails to move log
	to_delete = [] # emails to delete
		
	# select mailbox
	try:
		resp, data = imap_obj.select(mailbox)
		if resp != 'OK':
			raise imaplib.IMAP4.error('Could not find mailbox: ' + ", ".join([str(x) for x in resp[1]]))
	# search mailbox
		resp, data = imap_obj.search(None, '(SUBJECT "{}")'.format(subj_text))
		if resp != 'OK':
			return res # no email found
	# fetch data
		for itm in data[0].split():
			resp, email = imap_obj.fetch(itm,'(BODY.PEEK[TEXT])')
			if resp != 'OK':
				res.append('')
			else:
				res.append(email[0][1].decode('cp1250'))
				to_delete.append(itm)
	
	# delete fetched Emails
		if len(to_delete) > 0:
			res[1] = moveEmail(imap_obj,to_delete,'_Transakce') # unable to delete emails log
		
		return res
	
	except imaplib.IMAP4.error as e:
		raise Exception(e)
	finally:
		try:
			imap_obj.close() # selected inbox
			imap_obj.logout() # log out
			return res
		except imaplib.IMAP4.error as e:
			res[0] = exceptTraceback(e)

def moveEmail(imap_object, items_to_del,new_folder):
	"""
	move emails to designated mailbox folder
	return [1,3,4,10]
	where the numbers point to emails that could not be moved for an unspecified reason
	"""
	del_message = []
	del_res = []
	for it in items_to_del:
		try:
			imap_object.uid('COPY', it, new_folder)
			imap_object.store(it, '+FLAGS', '\\Deleted')
			del_message.append(0)
		except imaplib.IMAP4.error as e:
			del_message.append(1)
	# format deleted emails log message
	if sum(del_message) != 0:
		del_res = [ind+1 for ind,val in enumerate(del_message) if val==1]
	return del_res

def parseEmail(email_body):
	"""
	parse email body based on internal :-) regex conditions
	return a list [date, amount, currency]
	"""
	res = []
	try:
		found_date = re.findall(r'\d{1,2}\.\s?\d{1,2}\.\s?\d{1,4}\s?\d{1,2}:\d{1,2}',email_body)[0]
		found_amount = re.findall(r'(\d+)\s*[A-Z]+\.',email_body)[0]
		found_currency = re.findall(r'\d+\s*([A-Z]+)\.',email_body)[0]
	except Exception as e:
		raise Exception(e)
	return [found_date,found_amount,found_currency]
	

def sendMail(smtp_addr,port,credentials,FROM,FROM_nm,TO,TO_nm,subj,msg_txt):

	# res = ''
	try:
		smtpObj = smtplib.SMTP_SSL(smtp_addr,port)
		smtpObj.login(credentials[0],credentials[1])

		msg = MIMEText(msg_txt,'plain','utf-8')
		msg['Subject'] = Header(subj,'utf-8')
		msg['From'] = '{0} <{1}>'.format(Header(FROM_nm,'utf-8'),FROM)
		msg['To'] = '{0} <{1}>'.format(Header(TO_nm,'utf-8'),TO)

		smtpObj.sendmail(FROM,TO,msg.as_string().encode('ascii'))
		# res = True
		return True
	except Exception as e:
		raise Exception(e)
	finally:
		try:
			smtpObj.quit()
		except Exception as e:
			pass
