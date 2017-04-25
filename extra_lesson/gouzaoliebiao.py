#!/bin/python
L = []
M = []
n=1
while n<100:
	L.append(n)
	n = n+2

print L

for i in range(1,100):
	M.append(i)
print M
print len(M)
print M.__len__
