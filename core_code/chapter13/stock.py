#!/usr/bin/env python

from urllib2 import urlopen as uop
from time import ctime

TICKs = ('yhoo', 'dell', 'cost', 'adbe','intc', 'aple', 'goog', 'ebay', 'amzn')
url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print url % ','.join(TICKs)
print '\nPrices quoted as of :%s PDT\n' % ctime()
print 'TICKER', 'PRICE', 'CHANGE', '%AGE'
print '------', '-----', '------', '----'
u=uop(url % ','.join(TICKs))
print type(u)
for row in u:
    tick, price, chg, per = row.split(',')
    if price == 'N/A':
	print eval(tick), price, chg, eval(per),
        print '\n'
    else:
    	print eval(tick), '%.2f' % float(price), chg, eval(per),
        print '\n'

u.close()
