#!/usr/bin/env python
# encoding=utf8
import requests
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')
#r = requests.get("http://www.aispeech.com/")
r = requests.get("http://www.baidu.com/")
print r
print r.status_code
mm=r.text
f=open('hhhh.txt','w')
f.write(mm)
f.close()
file1 = open('hhhh.txt', 'r')
text = file1.read()
print text
print '==============='
kk = '<a href=\"http:\/\/(www..*)\">'
res = re.findall(kk,text)
res = str(res)
print type(res)
m=open('mm.txt', 'w')
m.write(res)
m.close()
