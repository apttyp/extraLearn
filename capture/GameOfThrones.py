#!/usr/bin/env python
# encoding=utf8
import requests
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')
#r = requests.get("http://www.aispeech.com/")
r = requests.get("http://www.ttmeiju.com/meiju/Game.of.Thrones.html")

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
kk = 'href=\"(magnet:.*)\srel='
res = re.findall(kk,text)
#print res
useful = []
for magnet in res:
#    if "Game.of.Thrones.S07E03" in magnet and "1080p" in magnet:
    if "Game.of.Thrones.S07E03" in magnet:
	useful.append(magnet)
print len(useful)
print useful
#print res[0]
#res = str(res)
#print type(res)
#m=open('mm.txt', 'w')
#m.write(res)
#m.close()
