#!/usr/bin/env python
def fib(max):
	n,a,b = 0,0,1
	while n< max:
		yield b
		a,b = b,a+b
		n = n+1
if __name__ == '__main__':
	print fib(6)	
