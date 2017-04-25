#!/usr/bin/env python
def ggg(x,y,f):
	return f(x)+f(y)

if __name__ == '__main__':
	print ggg(-3,4,abs)
