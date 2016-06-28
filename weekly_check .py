###########
# constants
from shared_constants import DAILY_LOG, WEEKLY_LOG, LAST_CHANCE_LOG, INTERVAL_DAILY
###########
from utils_log import logCheck

if __name__ == '__main__':
	subj = 'Era: chyba v 1. kontrolního skriptu (poslední zápis:'
	msg = 'Je třeba zkontrolovat 1. kontrolní skript.'
	log_msg = 'WEEKLY CHECK zjistil chybu, ale nebyl schopen odeslat mail.'
	log_err_msg = 've WEEKLY CHECKu se objevila chyba a skript nedoběhl'
	logCheck(DAILY_LOG,WEEKLY_LOG,LAST_CHANCE_LOG,INTERVAL_DAILY,subj,msg,log_msg,log_err_msg)