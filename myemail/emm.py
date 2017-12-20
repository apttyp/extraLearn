# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def sendsimplemail (warning):
        msg = MIMEText(warning)
        msg['Subject'] = 'Hello JinLong'
        msg['From'] = '18112619045@163.com'
        try:
                smtp = smtplib.SMTP()
                smtp.connect(r'smtp.163.com')
                smtp.login('18112619045@163.com', 'hehe123')
                smtp.sendmail('18112619045@163.com', ['jinlong.shi@aispeech.com'], msg.as_string())
                smtp.close()
		print "Send success!!!"
        except Exception, e:
                    print e

if __name__ == '__main__':
        sendsimplemail(warning = "ahaha")

