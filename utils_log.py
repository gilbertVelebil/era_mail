###########
# CONSTANTS
from shared_constants import (
	TIME_FORMAT,
	SMTP_ADDR, SMTP_PORT,
	CREDENTIALS_FILE,
	FROM, FROM_NM,
	TO, TO_NM)
###########

import os
from time import strptime, strftime, localtime
from datetime import datetime, timedelta
from py_mail import sendMail, getCredentials
from utils import exceptTraceback, absFilePath
import sqlite3

"""
(1) absFilePath
(2) logTime
(3) readTimeDifference
(4) logCheck
"""

def createTable(db,tbl_nm,tbl_definition,index_col=None):
	"""
	create a table (if it does not exist) in the given db based on the given definition
	optional: index column
	return: True (tbl created), False (tbl already existed)
	"""
	# try:
	ret = False
	con = sqlite3.connect(db)
	cur = con.cursor()
	cur.execute("PRAGMA table_info({0})".format(tbl_nm))

	if cur.fetchall() == []:
		ret = True
		cur.execute("CREATE TABLE {0} ({1};".format(tbl_nm,tbl_definition))
		if index_col != None:
			cur.execute("SELECT * FROM {0} LIMIT 1".format(tbl_nm))
			col_nm = [description[0] for description in cur.description][index_col]
			cur.execute("CREATE INDEX ind_{0} ON {1}({0});".format(col_nm,tbl_nm))
	# except Exception as e:
		# pass
		# raise Exception(e)
	return ret

def logTime(db,tbl_nm,time_format,*to_log):
	"""
	log datetime using the given format into a tbl plus fill in additional fields
	number of additional fields is truncated if necessary
	return True if OK
	"""
	con = sqlite3.connect(db)
	cur = con.cursor()
	
	# get colum names
	cur.execute("SELECT * FROM {0} LIMIT 1;".format(tbl_nm))
	col_nms = [description[0] for description in cur.description]
	
	dtime = strftime(time_format)
	cur.execute("INSERT INTO {0}({1}) VALUES ('{2}');".format(tbl_nm,col_nms[0],dtime))

	if to_log:
		for i,j in zip(to_log[:len(col_nms)],range(1,len(col_nms)+1)):
			cur.execute("INSERT INTO {0}({1}) VALUES ('{2}');".format(tbl_nm,col_nms[j],i))

	con.commit()
	return True

def readTimeDifference():
	pass



# def logTime(file_nm,time_format,optional_msg=''):
# 	"""
# 	logs current datetime in the given format to the given file
# 	returns True if everything's OK
# 	"""
# 	abs_file_path = absFilePath(file_nm)
# 	try:
# 		with open(abs_file_path,'a') as log:
# 			if optional_msg != '':
# 				optional_msg = ' {0} '.format(optional_msg)
# 			log.write(strftime(time_format) + optional_msg + '\n')
# 		return True
# 	except (FileNotFoundError, PermissionError) as e:
# 		raise Exception(exceptTraceback(e))


def readTimeDifference(file_nm,time_format):
	"""
	returns time difference (in seconds, integer) between now and datetime read from a log file
	"""
	abs_file_path = absFilePath(file_nm)
	try:
		with open(abs_file_path,'r') as log:
			# date/time to string
			str_datetime = log.readlines()[-1].rstrip()
			# from string to struct
			struct_datetime = strptime(str_datetime,time_format)
			# from struct to datetime
			datetime_datetime = datetime(*struct_datetime[:6])
			# timedelta from datetime
			now = datetime(*localtime()[:6])
			diff = now - datetime_datetime
			return diff.total_seconds()
	except Exception as e:
		raise Exception(exceptTraceback(e))

# @@@ je správné NEposílat do funkce SMTP_ADDR a další, které pak použije sendMail?
def logCheck(checked_log,supervising_log,last_chance_log,interval_sec,subj,msg,log_msg,log_err_msg):
	"""
	once in a specified period check the "junior" log:
		1) the datetime is younger than the specified interval >> OK, log time to the supervising log file and terminate,
		2) the datetime is older... (= the operational script didn't run as expected
			>> log time to the supervising log file and notify of doing so via email
		if sending notification mail fails, log to last-chance log file
		if there are other errors, log unspecified error into last-chance log file
	"""
	try:
		diff = readTimeDifference(checked_log,TIME_FORMAT)
		# 5 minute leeway (main script may take some time to run so that more than the sleep() amount of time usually elapses between the runs/logs)
		if diff <= interval_sec + 5 * 60:
			# OK, just log check time
			logTime(supervising_log,TIME_FORMAT)
		else:
			# the checked script may have not run as expected, notify via email
			credentials = getCredentials(CREDENTIALS_FILE)
			subj_formed = '{0} -{1} minut)'.format(subj,diff/60)
			snd_mess = sendMail(SMTP_ADDR,SMTP_PORT,credentials,FROM,FROM_NM,TO,TO_NM,subj_formed,msg)
			if snd_mess is not True:
				# email could not be send, at least log that
				logTime(last_chance_log,TIME_FORMAT,log_msg + ' -- Reason: ' + snd_mess + ' --')
	except Exception as e:
		# error occured while log-checking :-/
		# try notifying via email, if it doesn't work, the last_chance_log is, well, the only chance
		try:
			logTime(last_chance_log,TIME_FORMAT,log_err_msg + ': ' + str(e))
			sendMail(SMTP_ADDR,PORT,credentials,FROM,FROM_NM,TO,TO_NM,subj,msg_txt + ': ' + str(e))
		except:
			pass
			# what else can I do...