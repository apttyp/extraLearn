#!/bin/python
def fact(n):
         if n==1:
                 return 1
         else:
                 return n*fact(n-1)
 
if __name__ == '__main__': 
	sum1 = fact(1)
	print sum1
	sum2 = fact(2)
	print sum2
	sum3 = fact(5)
	print sum3
	sum4 = fact(1000)
	print sum4
