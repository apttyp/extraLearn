#!/usr/bin/env python

from urllib2 import urlopen as uop
from time import ctime
import time
import csv

TICKs = ('yhoo', 'dell', 'cost', 'adbe','intc', 'aple', 'goog', 'ebay', 'amzn')
url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

myintput = raw_input('Save to file(Y/N,y/n)?')

print url % ','.join(TICKs)
u=uop(url % ','.join(TICKs))
print type(u)

if myintput == 'Y' or myintput == 'y':
    print 'write to file'
    mytime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print mytime
    res = mytime+'.txt'
    
    with open(res, 'w') as f:
        for row in u:
            tick, price, chg, per = row.split(',')
            if price == 'N/A':
                f.write('%6s, %6s, %6s, %6s' %(eval(tick), price, chg, eval(per)))
                f.write('\n')
            else:
                f.write('%6s, %6s, %6s, %6s' %(eval(tick), '%.2f' % float(price), chg, eval(per)))
                f.write('\n')
    f.close()

#show on the screen
else:
    print '\nPrices quoted as of :%s PDT\n' % ctime()
    print 'TICKER', 'PRICE', 'CHANGE', '%AGE'
    print '------', '------', '------', '------'
    print u.read()
    #for row in u:
    #    tick, price, chg, per = row.split(',')
    #    if price == 'N/A':
    #    print '%6s, %6s, %6s, %6s' %(eval(tick), price, chg, eval(per))
    #    else:
    #	    print '%6s, %6s, %6s, %6s' %(eval(tick), '%.2f' % float(price), chg, eval(per))

u.close()
