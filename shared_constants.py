TIME_FORMAT = '%d. %m. %Y %H:%M'

"""
RUN_LOG = 'logs/run_log.txt'
DAILY_LOG = 'logs/daily_log.txt'
WEEKLY_LOG = 'logs/weekly_log.txt'
LAST_CHANCE_LOG = 'logs/error_log.txt'
"""
RUN_LOG = 'tbl_run_log'
DAILY_LOG = 'tbl_daily_log'
WEEKLY_LOG = 'tbl_weekly_log'
LAST_CHANCE_LOG = 'tbl_last_chance_log'

RUN_LOG_TBL_DEF = 'dtime TEXT PRIMARY KEY,found_emails_cnt INTEGER NOT NULL,fetched_emails_cnt INTEGER NOT NULL,processed_emails_cnt INTEGER NOT NULL,moved_emails_cnt INTEGER NOT NULL,error_msg TEXT)'
DAILY_LOG_TBL_DEF = 'dtime TEXT PRIMARY KEY,error_msg TEXT)'
WEEKLY_LOG_TBL_DEF = 'dtime TEXT PRIMARY KEY,error_msg TEXT)'
LAST_CHANCE_LOG_TBL_DEF = 'dtime TEXT PRIMARY KEY,error_msg TEXT)'

DFLT_DB = 'py_db.db'


INTERVAL_RUNNING =  0.5 * 60 * 60 # the interval (in seconds) for the main script
INTERVAL_DAILY =  24 * 60 * 60 # the interval (in seconds) for the daily check
#INTERVAL_WEEKLY =  7 * 24 * 60 * 60 # the interval (in seconds) for the weekly

IMAP_ADDR = 'imap.seznam.cz'
IMAP_PORT = 993

SMTP_ADDR = 'smtp.seznam.cz'
SMTP_PORT = 465
CREDENTIALS_FILE = 'py_mail_cred.txt'
FROM = 'Era'
FROM_NM = 'do.hrabal@post.cz'
TO = 'L.C.'
TO_NM = 'lukas.crhak@post.cz'

FOLDER = 'INBOX'
SAVE_TO_FOLDER = '_Transakce'