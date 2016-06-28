###########
# constants
from shared_constants import RUN_LOG, DAILY_LOG, LAST_CHANCE_LOG, INTERVAL_RUNNING
###########
from utils_log import logCheck

if __name__ == '__main__':
	subj = 'Era: chyba v běhu hlavního skriptu (poslední zápis:'
	msg = 'Je třeba zkontrolovat hlavní skript.'
	log_msg = 'DAILY CHECK zjistil chybu, ale nebyl schopen odeslat mail.'
	log_err_msg = 'v DAILY CHECKu se objevila chyba a skript nedoběhl'
	logCheck(RUN_LOG,DAILY_LOG,LAST_CHANCE_LOG,INTERVAL_RUNNING,subj,msg,log_msg,log_err_msg)