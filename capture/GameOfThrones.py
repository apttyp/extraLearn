#!/usr/bin/env python
# encoding=utf8
import requests
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    r = requests.get("http://www.ttmeiju.com/meiju/Game.of.Thrones.html")
    mm=r.text
    f=open('hhhh.txt','w')
    f.write(mm)
    f.close()
    file1 = open('hhhh.txt', 'r')
    text = file1.read()
    print text
    kk = 'href=\"(magnet:.*)\srel='
    res = re.findall(kk,text)
    useful = []
    for magnet in res:
#    if "Game.of.Thrones.S07E03" in magnet and "1080p" in magnet:
        if "Game.of.Thrones.S07E03" in magnet:
	    useful.append(magnet)
    print len(useful)
    print useful

if __name__ == '__main__':
    main()
