#!/usr/bin/env python
from time import ctime
from urllib2 import urlopen
import csv

TICKs = ('cost', 'adbe', 'intc', 'goog', 'ebay', 'amzn')
URL = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=sl1c1p2'

print '\nPrices quoted as of: %s PDT\n' % ctime()
print 'TICKER', 'PRICE', 'CHANGE', '%AGE'
print '------', '-----', '------', '----'
u = urlopen(URL % ','.join(TICKs))

reader = csv.reader(u)
for tick, price, chg, pct in reader:
    print tick.ljust(7), ('%.2f' % round(float(price), 2)).rjust(6), chg.rjust(6), pct.rstrip().rjust(6)
u.close()
