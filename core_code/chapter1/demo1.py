#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from string import ascii_uppercase as LC
from sys import maxint
from time import ctime
import os

tlds = ('com', 'edu', 'net', 'org', 'gov')

os.remove('redata.txt')

for i in xrange(randrange(5, 11)):
    dtint = randrange(2**32)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in xrange(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' %(dtstr, login, dom,choice(tlds), dtint, llen, dlen)
    with open('redata.txt', 'a') as f:
	f.write('%s::%s@%s.%s::%d-%d-%d' %(dtstr, login, dom,choice(tlds), dtint, llen, dlen))
	f.write('\r\n')
    	f.close()
