# @@@
# class ReadTimeDifferece(unittest.TestCase) - nelze spustit víc než 1 testovací funkci naráz; PROČ?

# from parent dir:
# python3 -m unittest -v test.test_file
# using -m, packages/modules can be specified in the usual way

	# @unittest.skip("demonstrating skipping")
	# @unittest.expectedFailure
import unittest
import unittest.mock as mock
import shared_constants as CONST
import os

def prnt(x):
	print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print(x)
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

###############
# py_mail.py
###############

####################################################
# @@@ replaced
# class GetCredentials(unittest.TestCase):
# 	credentials = ['do.hrabal@post.cz','904864']
# 	from src import py_mail

# 	def test_getCredentials_PASS(self):
# 		self.assertEqual(self.py_mail.getCredentials('src/py_mail_cred.txt'),self.credentials)
# 	def test_getCredentials_FAIL(self):
# 		self.assertNotEqual(self.py_mail.getCredentials('src/py_mail_cred_test_FOO.txt'),self.credentials)
# 	def test_getCredentials_FAIL_2(self):
# 		self.assertEqual(len(self.py_mail.getCredentials('src/py_mail_cred_test.txt')),1)
####################################################

# class GetCredentials(unittest.TestCase):
# 	CREDENTIALS = ['do.hrabal@post.cz','904864']
# 	import py_mail
# 	from unittest.mock import mock_open, patch
	
	# with mock.patch('builtins.open',m_open,create=True):
		# res = py_mail.getCredentials('xsrc/py_mail_cred.txt')
		# print(res)

	
	# m_open = mock_open(read_data='do.hrabal@post.cz 904864')
	# @mock.patch('builtins.open', m_open,create=True)
	# def test_getCredentials_PASS(self):
	# 	self.assertEqual(self.py_mail.getCredentials('py_mail_cred.txt'),self.CREDENTIALS)

	# # wrong file content
	# m_open = mock_open(read_data='fkjdlfjdlskjfl 9049830948')
	# @mock.patch('builtins.open',m_open,create=True)
	# def test_getCredentials_FAIL(self):
	# 	self.assertNotEqual(self.py_mail.getCredentials('py_mail_cred.txt'),self.CREDENTIALS)

	# # empty file
	# m_open = mock_open(read_data='')
	# @mock.patch('builtins.open',m_open,create=True)
	# def test_getCredentials_FAIL(self):
	# 	self.assertRaises(Exception,self.py_mail.getCredentials,'py_mail_cred.txt')
	
	# # credentials file does not exist
	# m_open = mock_open(read_data='fkjdlfjdlskjfl 9049830948')
	# m_open.side_effect = Exception()
	# @mock.patch('builtins.open', m_open,create=True)
	# def test_getCredentials_FAIL(self):
	# 	self.assertRaises(Exception,self.py_mail.getCredentials,'py_mail_cred.txt')

		
##########################################################################
# @@@ replaced
# class LoginMailTest(unittest.TestCase):
# 	def setUp(self):
# 		from src import py_mail
# 		self.py_mail = py_mail
# 		# test arguments:
# 		self.imap_srv = 'imap.seznam.cz'
# 		self.port = 993
# 		self.credentials = ['do.hrabal@post.cz','904864']
# 		# test against:
# 		self.resp = 'OK'
# 	def test_login(self):
# 		# length of returned list = 2 >> IMAP object has been created and returned as list[1]
# 		self.assertEqual(len(self.py_mail.loginMail(self.imap_srv,self.port,self.credentials)),2)
# 		# length of returned list = 1 >> only error log has been appended
# 		self.assertEqual(len(self.py_mail.loginMail('imap.google.cz',self.port,self.credentials)),1)
# 		self.assertEqual(len(self.py_mail.loginMail(self.imap_srv,self.port,['do.hrabal@sezn.cz','904864'])),1)
# 		self.assertEqual(len(self.py_mail.loginMail(self.imap_srv,self.port,['do.hrabal@post.cz','90486'])),1)
##########################################################################

# class LoginMailTest(unittest.TestCase):
# 	import imaplib
# 	import py_mail
			
	# @mock.patch('imaplib.IMAP4_SSL.login',autospec=True,return_value=['OK','some MASSAGE'])
	# def test_login_emails_PASS(self,m_login):
	# 	# return [<err_message>, IMAP object]
	# 	self.imap_obj  = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	# mocked object - check if called with desired arguments
	# 	# argument 1: instance on which the method is invoked
	# 	m_login.assert_called_with(self.imap_obj,'do.hrabal@post.cz','904864')
	# 	# check if tested function returns what it should
	# 	self.assertIsInstance(self.imap_obj,self.imaplib.IMAP4_SSL)

	# # wrong server info
	# @mock.patch('imaplib.IMAP4_SSL.login',autospec=True,return_value=['NOT OK',['some MASSAGE']])
	# def test_login_emails_FAIL_wrong_server(self,m_login):
	# 	self.assertRaises(Exception,self.py_mail.loginMail,'IMPA.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	assert not m_login.called
	
	# # could not log in
	# @mock.patch('imaplib.IMAP4_SSL.login',autospec=True,return_value=['NOT OK',['some MASSAGE']])
	# def test_login_emails_FAIL_couldnt_login(self,m_login):
	# 	# return [<err_message>, IMAP object]
	# 	self.assertRaises(Exception,self.py_mail.loginMail,'imap.seznam.cz',993,['doesnotexist@post.cz','wrongpswd'])
	# 	self.assertEqual(list(m_login.call_args[0][1:]), ['doesnotexist@post.cz','wrongpswd'])
	

# class GetEmailsTest(unittest.TestCase):
# 	import imaplib
# 	import py_mail

# 	@mock.patch('py_mail.moveEmail',autospec=True,return_value=['',''])
# 	@mock.patch('imaplib.IMAP4_SSL.select',autospec=True,return_value=['OK',['mailbox obj']])
# 	@mock.patch('imaplib.IMAP4_SSL.search',autospec=True,return_value=['OK',[b'email_obj1 email_obj2 email_obj3']])
# 	@mock.patch('imaplib.IMAP4_SSL.fetch',autospec=True,return_value=['OK',[[b'email_text1',b'email_text2',b'email_text3']]])
# 	def test_get_emails_PASS(self,m_fetch,m_search,m_select,m_move):
# 		# prep
# 		self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
# 		self.imap_obj = self.res_login
# 		# @@@
# 		self.expected_fetch_calls = [(b'email_obj1', '(BODY.PEEK[TEXT])',),
#  									(b'email_obj2', '(BODY.PEEK[TEXT])',),
#  									(b'email_obj3', '(BODY.PEEK[TEXT])',)]

# 		# run the function under test
# 		self.res = self.py_mail.getEmails(self.imap_obj,'INBOX','transakce',1)
# 		# assert
# 		m_select.assert_called_with(self.imap_obj,'INBOX')
# 		m_search.assert_called_with(self.imap_obj,None,'(SUBJECT "transakce")')
# 		m_fetch.call_count == 3
# 		# @@@ jak tam dostat ten IMAP4 object (první argument, protože se volá na instanci IMAP4...)???
# 		# provizorní řešení bez něj, jen s dalšími argumenty
# 		self.actual_fetch_calls = [args[0][1:] for args in m_fetch.call_args_list]
# 		self.assertEqual(self.actual_fetch_calls,self.expected_fetch_calls)
	
	# # wrong mailbox name
	# @mock.patch('imaplib.IMAP4_SSL.search',autospec=True,return_value=['OK',[b'email_obj1 email_obj2 email_obj3']])
	# @mock.patch('imaplib.IMAP4_SSL.select',autospec=True,return_value=['NOT OK',['mailbox obj']])
	# def test_get_emails_FAIL_wrong_mailbox(self,m_select,m_search):
	# 	# prep
	# 	self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	self.imap_obj = self.res_login
	# 	# run the function under test and test if exception has been thrown
	# 	self.assertRaises(Exception,self.py_mail.getEmails,self.imap_obj,'XXX_INBOX','transakce',1)
	# 	# assert
	# 	m_select.assert_called_with(self.imap_obj,'XXX_INBOX')
	# 	assert not m_search.called
	
	# # nothing found while searching
	# @mock.patch('imaplib.IMAP4_SSL.fetch',autospec=True,return_value=['OK',[[b'email_text1',b'email_text2',b'email_text3']]])
	# @mock.patch('imaplib.IMAP4_SSL.search',autospec=True,return_value=['NOT OK',[b'email_obj1 email_obj2 email_obj3']])
	# @mock.patch('imaplib.IMAP4_SSL.select',autospec=True,return_value=['OK',['mailbox obj']])
	# def test_get_emails_PASS_no_mail_found(self,m_select,m_search,m_fetch):
	# 	# prep
	# 	self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	self.imap_obj = self.res_login
	# 	# run the function under test
	# 	self.res = self.py_mail.getEmails(self.imap_obj,'INBOX','transakce',1)
	# 	# assert
	# 	m_select.assert_called_with(self.imap_obj,'INBOX')
	# 	self.assertEqual(type(self.res[0][0]),self.imaplib.IMAP4.error)
	# 	self.assertEqual(self.res[1],'')
	# 	assert not m_fetch.called

	# # nothing fetched
	# @mock.patch('py_mail.moveEmail',autospec=True,return_value=['',''])
	# @mock.patch('imaplib.IMAP4_SSL.fetch',autospec=True,return_value=['NOT OK',[[b'email_text1',b'email_text2',b'email_text3']]])
	# @mock.patch('imaplib.IMAP4_SSL.search',autospec=True,return_value=['OK',[b'email_obj1 email_obj2 email_obj3']])
	# @mock.patch('imaplib.IMAP4_SSL.select',autospec=True,return_value=['OK',['mailbox obj']])
	# def test_get_emails_FAIL_no_mail_fetched(self,m_select,m_search,m_fetch,m_move):
	# 	# prep
	# 	self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	self.imap_obj = self.res_login # [0] is always the self object here
	# 	# run the function under test
	# 	self.res = self.py_mail.getEmails(self.imap_obj,'XXX_INBOX','transakce',1)
	# 	# assert
	# 	m_select.assert_called_with(self.imap_obj,'XXX_INBOX')
	# 	self.assertEqual(m_search.call_args[0][1:],(None,'(SUBJECT "transakce")'))
	# 	# assert not m_move.called
	# 	self.assertEqual(type(self.res[0][0]),self.imaplib.IMAP4.error)
	# 	self.assertEqual(self.res[1:],['','','','']) # no move email error + plus three empty slots for emails that were found but not fetched


# class MoveEmailsTest(unittest.TestCase):
# 	import imaplib
# 	import py_mail

# 	@mock.patch('imaplib.IMAP4_SSL.uid',autospec=True)
# 	@mock.patch('imaplib.IMAP4_SSL.store',autospec=True)
# 	def test_move_emails_PASS(self,m_store,m_uid):
# 		# prep
# 		self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
# 		self.imap_obj = self.res_login # [0] is always the self object here
# 		# run the function under test
# 		self.assertFalse(self.py_mail.moveEmail(self.imap_obj,['email_to_del1','email_to_del2','email_to_del3'],'_Transakce'))

# 	@mock.patch('imaplib.IMAP4_SSL.uid',autospec=True)
# 	@mock.patch('imaplib.IMAP4_SSL.store',autospec=True)
# 	def test_get_emails_FAIL_store(self,m_store,m_uid):
# 		# prep
# 		self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
# 		self.imap_obj = self.res_login # [0] is always the self object here
# 		m_store.side_effect = self.imaplib.IMAP4.error
# 		# run the function under test
# 		self.assertTrue(self.py_mail.moveEmail(self.imap_obj,['email_to_del1','email_to_del2','email_to_del3'],'_Transakce'))

	# @mock.patch('imaplib.IMAP4_SSL.uid',autospec=True)
	# @mock.patch('imaplib.IMAP4_SSL.store',autospec=True)
	# def test_get_emails_FAIL_uid(self,m_store,m_uid):
	# 	# prep
	# 	self.res_login = self.py_mail.loginMail('imap.seznam.cz',993,['do.hrabal@post.cz','904864'])
	# 	self.imap_obj = self.res_login # [0] is always the self object here
	# 	m_uid.side_effect = self.imaplib.IMAP4.error
	# 	# run the function under test
	# 	self.assertTrue(self.py_mail.moveEmail(self.imap_obj,['email_to_del1','email_to_del2','email_to_del3'],'_Transakce'))

# class ParseEmailsTest(unittest.TestCase):
# 	import imaplib
# 	import py_mail
# 	BODY = """
# Dobrý den,

# 29. 4. 2016 19:03 byla provedena autorizace transakce platební kartou číslo '*5765' na částku 82 CZK.

# V případě dotazů, týkajících se Vaší platební karty, kontaktujte prosím Klientské centrum Ery/Poštovní spořitelny na telefonním čísle 495 800 121.

# Vaše Era
# www.erasvet.cz, 800 210 210
# Era je obchodní značka ČSOB.
# 		"""
	# def test_parse_emails_PASS(self):
	# 	# prep
	# 	self.res = self.py_mail.parseEmail(self.BODY)
	# 	# run the function under test
	# 	self.assertTrue(self.res == ['29. 4. 2016 19:03','82','CZK'])
			
	# def test_parse_emails_FAIL(self):
	# 	# prep
	# 	self.assertRaises(Exception,self.py_mail.parseEmail,'nějaký text mailu, který neobsahuje, co obsahovat má')

		
# class SendEmail(unittest.TestCase):
# 	import smtplib
# 	import py_mail
# 	SMTPsrv = CONST.SMTP_ADDR
# 	PORT = CONST.SMTP_PORT
# 	CREDENTIALS = ['do.hrabal@post.cz','904864']
# 	FROM = CONST.FROM
# 	FROM_nm = CONST.FROM_NM
# 	TO = CONST.TO
# 	TO_nm = 'LC_test'
# 	SUBJ = 'Platba: {0} {1} ({2})'.format('82','CZK','2. 5. 2015 19.36')
# 	MESS = ''
# 	MESS_TEXT =  b'Content-Type: text/plain; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nSubject: =?utf-8?b?UGxhdGJhOiA4MiBDWksgKDIuIDUuIDIwMTUgMTkuMzYp?=\nFrom: do.hrabal@post.cz <Era>\nTo: LC_test <L.C.>\n\n'

	# @mock.patch('smtplib.SMTP_SSL.login',autospec=True)
	# @mock.patch('smtplib.SMTP_SSL.sendmail',autospec=True)
	# @mock.patch('smtplib.SMTP_SSL.quit',autospec=True)
	# def test_send_PASS(self,m_quit,m_send,m_login):
	# 	self.res = self.py_mail.sendMail(self.SMTPsrv,self.PORT,self.CREDENTIALS,self.FROM,self.FROM_nm,self.TO,self.TO_nm,self.SUBJ,self.MESS) # returns True if everything is OK
	# 	self.assertTrue(self.res is True)
	# 	self.assertTrue(m_login.call_args[0][1:] == tuple(self.CREDENTIALS))
	# 	self.assertTrue(m_send.call_args[0][1:] == (self.FROM,self.TO,self.MESS_TEXT)) # first call_arg is an SMTP object (which never leaves the scope of the function)
	# 	self.assertTrue(m_quit.called)

	# # wrong login arguments
	# @mock.patch('smtplib.SMTP_SSL.sendmail',autospec=True)
	# @mock.patch('smtplib.SMTP_SSL.quit',autospec=True)
	# def test_send_FAIL_wrong_login(self,m_quit,m_send):
	# 	self.assertRaises(Exception,self.py_mail.sendMail,self.SMTPsrv,self.PORT,'wrong_login',self.FROM,self.FROM_nm,self.TO,self.TO_nm,self.SUBJ,self.MESS)
	# 	self.assertFalse(m_send.called)
	# 	self.assertTrue(m_quit.called)

	# # wrong sendmail arguments
	# # (note: side_effect must be an iterable...; here, one call only is expected so [] is enough)
	# @mock.patch('smtplib.SMTP_SSL.sendmail',autospec=True,side_effect=[Exception('some sendmail exception')])
	# @mock.patch('smtplib.SMTP_SSL.quit',autospec=True)
	# def test_send_FAIL_wrong_sendmail_args(self,m_quit,m_send):
	# 	self.assertRaises(Exception,self.py_mail.sendMail,self.SMTPsrv,self.PORT,self.CREDENTIALS,self.FROM,self.FROM_nm,self.TO,self.TO_nm,self.SUBJ,self.MESS) # returns True if everything is OK
	# 	self.assertTrue(m_send.called)
	# 	self.assertTrue(m_quit.called)

	# # quit() raises an exception
	# # (note: side_effect must be an iterable...; here, one call only is expected so [] is enough)
	# @mock.patch('smtplib.SMTP_SSL.sendmail',autospec=True)
	# @mock.patch('smtplib.SMTP_SSL.quit',autospec=True,side_effect=[Exception('some quit() exception')])
	# def test_send_FAIL_quit_exception(self,m_quit,m_send):
	# 	self.res = self.py_mail.sendMail(self.SMTPsrv,self.PORT,self.CREDENTIALS,self.FROM,self.FROM_nm,self.TO,self.TO_nm,self.SUBJ,self.MESS) # returns True if everything is OK
	# 	self.assertTrue(self.res is True)
	# 	self.assertTrue(m_send.called)
	# 	self.assertTrue(m_quit.called)


###############
# utils.py
###############

# class AbsoluteFilePath(unittest.TestCase):
# 	import utils_log
# 	REL_PATH = 'subfolder/file1.txt'
# 	REL_PATH_TEST =  'test/subfolder/file1.txt'
# 	ABS_PATH = os.path.join(os.path.dirname(__file__), REL_PATH)
	
# 	def test_file_path_PASS(self):
# 		print('\n\n')
# 		self.assertTrue(self.utils_log.absFilePath(self.REL_PATH_TEST) == self.ABS_PATH)

# 	def test_file_path_FAIL(self):
# 		print('\n\n')
# 		self.assertFalse(self.utils_log.absFilePath(self.REL_PATH_TEST) == 'completely unrelated path')



###############
# utils_log.py
###############

# @mock.patch('utils_log.sqlite3',autospec=True)
# class CreateTable(unittest.TestCase):
# 	import utils_log
# 	import sqlite3
# 	from unittest.mock import patch
# 	from shared_constants import DFLT_DB, RUN_LOG, RUN_LOG_TBL_DEF

# 	# tbl does not exist yet
# 	def test_createTable_PASS(self,m_sqlite):
# 		m_sqlite.connect().cursor().fetchall.return_value = []
# 		res = self.utils_log.createTable(self.DFLT_DB,self.RUN_LOG,self.RUN_LOG_TBL_DEF)
# 		self.assertTrue(res)
# 		self.assertTrue(m_sqlite.connect().cursor().execute.call_count==2)


# 	# tbl does not exist yet, create with index
# 	def test_createTable_PASS_with_index(self,m_sqlite):
# 		m_sqlite.connect().cursor().fetchall.return_value = []
# 		m_sqlite.connect().cursor().description = [['dtime',0],['col2',0],['col3',0],['col4',0]]
# 		res = self.utils_log.createTable(self.DFLT_DB,self.RUN_LOG,self.RUN_LOG_TBL_DEF,0)
# 		self.assertTrue(res)
# 		self.assertTrue(m_sqlite.connect().cursor().execute.call_count==4)

# 	# tbl does exist, nothing created
# 	def test_createTable_PASS_tbl_exists(self,m_sqlite):
# 		m_sqlite.connect().cursor().fetchall.return_value = ['some value that indicates the table already exists']
# 		res = self.utils_log.createTable(self.DFLT_DB,self.RUN_LOG,self.RUN_LOG_TBL_DEF,0)
# 		self.assertFalse(res)
# 		self.assertTrue(m_sqlite.connect().cursor().execute.call_count==1)

# 	# exception thrown - wrong index column number
# 	def test_createTable_FAIL(self,m_sqlite):
# 		pass
# 		m_sqlite.connect().cursor().fetchall.return_value = []
# 		m_sqlite.connect().cursor().description = [['dtime',0],['col2',0],['col3',0],['col4',0]]
# 		self.assertRaises(Exception,self.utils_log.createTable,self.DFLT_DB,self.RUN_LOG,self.RUN_LOG_TBL_DEF,4)
# 		self.assertTrue(m_sqlite.connect().cursor().execute.call_count==3)

@mock.patch('utils_log.strftime',autospec=True,return_value='08. 06. 2016 20:11')
@mock.patch('utils_log.sqlite3',autospec=True)
class LogTime(unittest.TestCase):
	import utils_log
	import sqlite3
	from unittest.mock import patch, call
	from shared_constants import DFLT_DB, RUN_LOG, RUN_LOG_TBL_DEF, TIME_FORMAT

	# FAIL
	# 

	# # logs datetime only
	# def test_logTime_PASS_datetime(self,m_sqlite,m_strftime):
	# 	m_sqlite.connect.return_value.cursor.return_value.description = [['dtime',0],['found_emails_cnt',0],['fetched_emails_cnt',0],['processed_emails_cnt',0],['moved_emails_cnt',0],['error_msg',0]]
	# 	self.res = self.utils_log.logTime(self.DFLT_DB,self.RUN_LOG,self.TIME_FORMAT)
	# 	self.expected_exec_1 = "SELECT * FROM tbl_run_log LIMIT 1;"
	# 	self.expected_exec_2 = "INSERT INTO tbl_run_log(dtime) VALUES ('08. 06. 2016 20:11');"
	# 	self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list[0][0][0],self.expected_exec_1)
	# 	self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list[1][0][0],self.expected_exec_2)

	# logs datetime + additional columns
	def test_logTime_PASS_datetime_logs(self,m_sqlite,m_strftime):
		m_sqlite.connect.return_value.cursor.return_value.description = [['dtime',0],['found_emails_cnt',0],['fetched_emails_cnt',0],['processed_emails_cnt',0],['moved_emails_cnt',0],['error_msg',0]]
		self.res = self.utils_log.logTime(self.DFLT_DB,self.RUN_LOG,self.TIME_FORMAT,10,10,10,10,'null')
		# self.expected_exec_1 = "SELECT * FROM tbl_run_log LIMIT 1;"
		# self.expected_exec_2 = "INSERT INTO tbl_run_log(dtime) VALUES ('08. 06. 2016 20:11');"
		# self.expected_exec_3 = "INSERT INTO tbl_run_log(found_emails_cnt) VALUES ('10');"
		# self.expected_exec_4 = "INSERT INTO tbl_run_log(fetched_emails_cnt) VALUES ('10');"
		# self.expected_exec_5 = "INSERT INTO tbl_run_log(processed_emails_cnt) VALUES ('10');"
		# self.expected_exec_6 = "INSERT INTO tbl_run_log(moved_emails_cnt) VALUES ('10');"
		# self.expected_exec_7 = "INSERT INTO tbl_run_log(error_msg) VALUES ('null');"
		self.expected_exec = [call("SELECT * FROM tbl_run_log LIMIT 1;"),
		self.call("INSERT INTO tbl_run_log(dtime) VALUES ('08. 06. 2016 20:11');"),
		self.call("INSERT INTO tbl_run_log(found_emails_cnt) VALUES ('10');"),
		self.call("INSERT INTO tbl_run_log(fetched_emails_cnt) VALUES ('10');"),
		self.call("INSERT INTO tbl_run_log(processed_emails_cnt) VALUES ('10');"),
		self.call("INSERT INTO tbl_run_log(moved_emails_cnt) VALUES ('10');"),
		self.call("INSERT INTO tbl_run_log(error_msg) VALUES ('null');")]
		# self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list[0][0][0],self.expected_exec_1)
		# self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list[1][0][0],self.expected_exec_2)
		# self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list,)
		# self.assertEqual(m_sqlite.connect.return_value.cursor.return_value.execute.call_args_list,self.expected_exec)



	# # logs datetime + additional columns - trims excess to_log information
	# def test_logTime_PASS_datetime_logs_trim(self,m_sqlite):
	# 	pass


# class LogTime(unittest.TestCase):
# 	import utils_log
# 	from unittest.mock import mock_open, patch
# 	TIME_FORMAT = CONST.TIME_FORMAT

# 	m_open = mock.mock_open()

# 	@mock.patch('utils_log.absFilePath',autospec=True,return_value='some_file1.txt')
# 	@mock.patch('builtins.open', m_open,create=True)
# 	def test_logTime_PASS(self,m_absFilePath):
# 		self.assertTrue(self.utils_log.logTime('some_unrelated_file',self.TIME_FORMAT))

	# @@@ vymyslet FAIL - neexistující soubor se vždycky nově vytvoří :-)
	# @mock.patch('utils_log.absFilePath',autospec=True,return_value='some_file1.txt')
	# def test_logTime_FAIL(self,m_absFilePath):
	# 	self.res = self.utils_log.logTime('some_unrelated_file',self.TIME_FORMAT)
		# self.assertTrue(self.res != True)

# class ReadTimeDifferece(unittest.TestCase):
# 	import utils_log
# 	import time
# 	from unittest.mock import mock_open, patch
# 	TIME_FORMAT = CONST.TIME_FORMAT

# 	m_open = mock.mock_open(read_data='1111\n2222\n25. 2. 2016 23:12')

	# # @@@ tenhle a následující test nejde spusti dohromady - PROČ?
	# @mock.patch('utils_log.localtime',autospec=True,return_value=time.strptime('27. 2. 2016 23:12',TIME_FORMAT))
	# @mock.patch('builtins.open',m_open,create=True)
	# def test_readTimeDiff_PASS(self,m_localtime):
	# 	self.res = self.utils_log.readTimeDifference('some file',self.TIME_FORMAT)
	# 	m_localtime.assert_called_with()
	# 	self.assertTrue(self.res == 172800.0)

	# # wrong difference
	# @mock.patch('utils_log.localtime',autospec=True,return_value=time.strptime('27. 2. 2035 23:12',TIME_FORMAT))
	# @mock.patch('builtins.open',m_open,create=True)
	# def test_readTimeDiff_FAILL_diff(self,m_localtime):
	# 	self.res = self.utils_log.readTimeDifference('some file',self.TIME_FORMAT)
	# 	m_localtime.assert_called_with()
	# 	self.assertFalse(self.res == 172800.0)

	# # wrong file contents
	# m_open = mock.mock_open(read_data='1111\n2222\n3333')	
	# @mock.patch('utils_log.localtime',autospec=True,return_value=time.strptime('27. 2. 2016 23:12',TIME_FORMAT))
	# @mock.patch('builtins.open', m_open,create=True)
	# def test_readTimeDiff_FAILL_diff(self,m_localtime):
	# 	self.assertRaises(Exception, self.utils_log.readTimeDifference,'some file',self.TIME_FORMAT)

	# # open non-existing file
	# @mock.patch('utils_log.localtime',autospec=True,return_value=time.strptime('27. 2. 2016 23:12',TIME_FORMAT))
	# def test_readTimeDiff_FAILL_diff(self,m_localtime):
	# 	self.assertRaises(Exception, self.utils_log.readTimeDifference, 'some non-existing file',self.TIME_FORMAT)


# class LogCheck(unittest.TestCase):
# 	import utils_log
# 	import py_mail
# 	import time
# 	from unittest.mock import mock_open, patch
# 	TIME_FORMAT = CONST.TIME_FORMAT
# 	CREDENTIALS = ['do.hrabal@post.cz','904864']

	# # OK, just log
	# @mock.patch('utils_log.readTimeDifference',autospec=True,return_value=2500)
	# @mock.patch('utils_log.logTime',autospec=True,return_value=True)
	# @mock.patch('py_mail.getCredentials',autospec=True,return_value=CREDENTIALS)
	# @mock.patch('py_mail.sendMail',autospec=True,return_value=True)
	# def test_logCheck_PASS(self,m_sendMail,m_getCredentials,m_logTime,m_readTimeDifference):
	# 	self.res = self.utils_log.logCheck('checked_log','supervising_log','last_chance_log',
	# 		2500,'couldnt log subj','couldnt log mgs',
	# 		'couldnt send error',
	# 		'some error log message')
	# 	self.assertIsNone(self.res)
	# 	self.assertFalse(m_sendMail.called)
	# 	m_logTime.assert_called_with('supervising_log',self.TIME_FORMAT)
	
	# # not OK, time difference too big, notify via email
	# @mock.patch('utils_log.readTimeDifference',autospec=True,return_value=5500)
	# @mock.patch('utils_log.logTime',autospec=True,return_value=True)
	# @mock.patch('utils_log.getCredentials',autospec=True,return_value=CREDENTIALS)
	# @mock.patch('utils_log.sendMail',autospec=True,return_value=True)
	# def test_logCheck_FAIL_larger_diff(self,m_sendMail,m_getCredentials,m_logTime,m_readTimeDifference):
	# 	self.res = self.utils_log.logCheck('checked_log','supervising_log','last_chance_log',
	# 		2500, 'couldnt log subj','couldnt log msg',
	# 		'couldnt send error',
	# 		'some error log message')
	# 	self.assertIsNone(self.res)
	# 	self.assertFalse(m_logTime.called)
	# 	m_sendMail.assert_called_with(CONST.SMTP_ADDR,CONST.SMTP_PORT,
	# 		self.CREDENTIALS,
	# 		CONST.FROM,CONST.FROM_NM,
	# 		CONST.TO,CONST.TO_NM,
	# 		 'couldnt log subj -91.66666666666667 minut)','couldnt log msg')
	
	# # not OK, time difference too big + couldn't notify via email >> log that
	# @mock.patch('utils_log.readTimeDifference',autospec=True,return_value=5500)
	# @mock.patch('utils_log.logTime',autospec=True,return_value=True)
	# @mock.patch('utils_log.getCredentials',autospec=True,return_value=CREDENTIALS)
	# @mock.patch('utils_log.sendMail',autospec=True,return_value='some email sending error') # Exception string is actually returned
	# def test_logCheck_FAIL_larger_diff_couldnt_email(self,m_sendMail,m_getCredentials,m_logTime,m_readTimeDifference):
	# 	self.res = self.utils_log.logCheck('checked_log','supervising_log','last_chance_log',
	# 		2500, 'couldnt log subj','couldnt log msg',
	# 		'couldnt send error',
	# 		'some error log message')
	# 	self.assertIsNone(self.res)
	# 	# self.assertFalse(m_logTime.called)
	# 	self.assertTrue(m_sendMail.called)
	# 	m_logTime.assert_called_with('last_chance_log',self.TIME_FORMAT,'couldnt send error -- Reason: some email sending error --')

	# # not OK, time difference too big + couldn't notify via email + couldn't log that (for whatever reason) >> log general error + notify via email
	# @mock.patch('utils_log.readTimeDifference',autospec=True,return_value=5500)
	# @mock.patch('utils_log.logTime',autospec=True,return_value=True)
	# @mock.patch('utils_log.getCredentials',autospec=True,return_value=None) # the error
	# @mock.patch('utils_log.sendMail',autospec=True,return_value='some email sending error',side_effect=Exception)
	# def test_logCheck_FAIL_larger_diff_couldnt_email(self,m_sendMail,m_getCredentials,m_logTime,m_readTimeDifference):
	# 	self.res = self.utils_log.logCheck('checked_log','supervising_log','last_chance_log',
	# 		2500, 'couldnt log subj','couldnt log msg',
	# 		'couldnt send error',
	# 		'some error log message')
	# 	self.assertIsNone(self.res)
	# 	m_logTime.assert_called_with('last_chance_log',self.TIME_FORMAT,'some error log message: ') # Exception str is mocked as empty

# 	# not OK, time difference too big + couldn't notify via email + couldn't log that >> log general error BUT couldn't notify via email
	# @@@ jak zařídit, aby vtniřní funkce (logTime) jednou spadla a podruhé běžela?




###################
# daily_checklog.py
###################


####################
# weekly_checklog.py
####################


####################
# main_script.py
####################




# if __name__ == '__main__':
# 	unittest.main()