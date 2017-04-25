#!/bin/python

def adjust_tool(n):
	i = 2;
	if n==1:
		return False
	while n-i>0:
		if n%i==0:
			return False
		else:
			i = i + 1
	return True
print filter(adjust_tool, range(1,100))	
