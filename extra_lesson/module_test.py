#!/bin/bin/env python
# *-* coding: utf-8 -*-
'a test module'

__author__ = 'Tonny'

import sys
def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello World!'
	elif args[1] == __author__:
		print 'Hello, %s!' % __author__
	else:
		print 'Too many'

if __name__ == '__main__':
	test()
