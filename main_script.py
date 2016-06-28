###########
# constants
from shared_constants import TIME_FORMAT, RUN_LOG, LAST_CHANCE_LOG,
	INTERVAL_RUNNING,
	IMAP_ADDR, IMAP_PORT, SMPT_ADDR, SMTP_PORT,
	CREDENTIALS_FILE,
	FROM, FROM_NM,
	TO, TO_NM,
	FOLDER,
	SAVE_TO_FOLDER

from utils_log import logTime, absFilePath
from py_mail import sendMail
from time import sleep

def main_loop():
	try:
		while 1:
			credentials =  getCredentials(CREDENTIALS_FILE)
			imap_obj = loginMail(IMAP_ADDR,IMAP_PORT,credentials)
			if imap_obj[0] == '':
				rslt = getEmails(imap_obj[1],FOLDER,'platba kartou',0)
				if rslt >= 3:
					for mail_body in rslt[2:]:
						parsed = parseEmail(mail_body)
						if len(parsed) != 3:
							parsed = [parsed,'~CHYBA~']
						send_res = sendMail(SMTP_ADDR,PORT,credentials,FROM,FROM_NM,TO,TO_NM,'Platba: {0} {1} ({2})'.format(parsed[1],parsed[2]),parsed[0])
			else:
				raise Exception(imap_obj[0])
	except Exception as e:
		try:
			credentials = getCredentials(CREDENTIALS_FILE)
			if len(credentials) == 2:
				if sendMail(SMTP_ADDR,PORT,CREDENTIALS,FROM,FROM_NM,TO,TO_NM,'Era: chyba v běhu hlavního skriptu','Popis chyby: {0}'.format(e)) != True:
					raise Exception
		exception Exception as e:
			logTime(LAST_CHANCE_LOG,TIME_FORMAT,'chyba v běhu hlavního skriptu ({0})'.format(e))
	finally:
		sleep(INTERVAL_RUNNING)

if __name__ == '__main__':
	try:
		# clear run_log and log current time
		abs_file_nm = absFilePath(RUN_LOG)
		open(abs_file_nm,'w').close()
		logTime(RUN_LOG,TIME_FORMAT)
		# enter the main loop
		main_loop()
	except Exception as e:
		try:
			credentials = getCredentials(CREDENTIALS_FILE)
			if len(credentials) == 2:
				if sendMail(SMTP_ADDR,PORT,CREDENTIALS,FROM,FROM_NM,TO,TO_NM,'Era: chyba při zavádění hlavního skriptu','Popis chyby: {0}'.format(e)) != True:
					raise Exception
		exception Exception as e:
			logTime(LAST_CHANCE_LOG,TIME_FORMAT,'chyba v zavádění hlavního skriptu ({0})'.format(e))