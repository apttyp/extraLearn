# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

def sendsimplemail (warning):
        msg = MIMEText(warning)
        msg['Subject'] = '见字如面'
        msg['From'] = 'xxx@163.com'
        try:
                smtp = smtplib.SMTP()
                smtp.connect(r'smtp.163.com')
                smtp.login('xxx@163.com', 'password')
                smtp.sendmail('xxx@163.com', ['xx@qq.com'], msg.as_string())
                smtp.close()
		print "Send success!!!"
        except Exception, e:
                    print e

if __name__ == '__main__':
        sendsimplemail(warning = "TYP:Just Let it go!")

