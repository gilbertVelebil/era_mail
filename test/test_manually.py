import py_mail as PM
import shared_constants as SH

# getting credentials
credentials =  PM.getCredentials(SH.CREDENTIALS_FILE)
print(credentials)

# creating imap_obj
imap_obj = PM.loginMail(SH.IMAP_ADDR,SH.IMAP_PORT,credentials)
print(imap_obj)
# 		rslt = getEmails(imap_obj,FOLDER,'platba kartou',0)
# 			for mail_body in rslt[2:]:
# 				parsed = parseEmail(mail_body)
# 				if len(parsed) != 3:
# 					parsed = [parsed,'~CHYBA~']
# 				send_res = sendMail(SMTP_ADDR,PORT,credentials,FROM,FROM_NM,TO,TO_NM,'Platba: {0} {1} ({2})'.format(parsed[1],parsed[2]),parsed[0])
# 		sleep(INTERVAL_RUNNING)
# # getting mails

# # 