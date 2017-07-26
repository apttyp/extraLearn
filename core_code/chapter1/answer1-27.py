#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from string import ascii_uppercase as LC
from sys import maxint
from time import ctime
import re

pat1 = '\s\w+\s'
pat2 = '\s\d+\s'
pat3 = '\s\d\d\d\d'

with open('redata.txt', 'r') as f:
    for line in f.readlines():
	mon = re.search(pat1, line).group()
	mystr = mon
	day = re.search(pat2, line).group()
	mystr = mystr+','+day
	year = re.search(pat3, line).group()
	mystr = mystr+','+year
	mystr = re.sub(' ', '', mystr)
	print mystr
