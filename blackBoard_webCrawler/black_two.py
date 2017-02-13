# encoding: UTF-8
#Blackboardsecond lesson
import requests
#avoid UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 108: ordinal not in range(128)
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
# r = requests.get(url)
x=1
while x<=20:
    m = str(x)
    print m
    payload = {'username': 'value1', 'password': m}
    print payload
    r = requests.post(url,data=payload)
    res = r.text
    sample1 = "密码错误"
    sample2 = "只有数字哦"
    if res.find(sample1) == -1 and res.find(sample2) == -1:
        print res
        print "GG"
        break
    else:
        x=x+1