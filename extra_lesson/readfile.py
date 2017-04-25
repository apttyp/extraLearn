#!/bin/python

import sys
import os
def myread():
	args = sys.argv
	print args
	if len(args)==1:
		print 'Please input file'	
	elif os.path.exists(args[1]):
		with open(args[1],'r') as f:
			#print f.read()
			print 'Begin to read file:'
			print '********************'
			for line in f.readlines():
				print line.strip()
			print '********************'
	else:
		print 'Too many'

if __name__ == '__main__':
	myread()
