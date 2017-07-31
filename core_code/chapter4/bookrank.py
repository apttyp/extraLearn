#!/usr/bin/env 
# encoding=utf8
from time import ctime, sleep
from atexit import register
from re import compile
from threading import Thread
from urllib2 import urlopen as uopen
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937':'Core Python Programming',
    '0132356139':'Python Web Development with Django',
    '0137143419':'Python Fundamentals',
}

def getRanking(isbn):
    print AMZN+isbn
    r = requests.get(AMZN+isbn)
    #page = uopen('%s%s' % (AMZN, isbn)) #str.format()
    data = r.text
    r.close()
    #file1 = open('all.txt', 'w')
    #file1.write(data)
    #file1.close()
    #print data
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print '- %r ranked %s' % (ISBNs[isbn], getRanking(isbn))

def main():
    print 'At', ctime(), 'On Amazon...'
    for isbn in ISBNs:
	_showRanking(isbn)

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
