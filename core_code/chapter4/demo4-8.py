#!/usr/bin/env 

from time import ctime, sleep
from myThread import MyThread

def fib(x):
    sleep(0.005)
    if x<2: return 1
    return (fib(x-2)+fib(x-1))

def fac(x):
    sleep(0.1)
    if x<2: return 1
    return (x * fac(x-1))

def mysum(x):
    sleep(0.1)
    if x<2: return 1
    return (x+mysum(x-1))

funcs = [fib, fac, mysum]
n=12

def main():
    nfuncs = range(len(funcs))
    print '###Singal Thread:'
    for i in nfuncs:
	print funcs[i].__name__, 'starting at:', ctime()
	print funcs[i](n)
	print funcs[i].__name__, 'finished at:', ctime()

    print '###Multiple Thread:'
    threads = []
    for i in nfuncs:
	t = MyThread(funcs[i], n, funcs[i].__name__)
	threads.append(t)
    for i in nfuncs:
	threads[i].start()

    for i in nfuncs:
	threads[i].join()
	print threads[i].getResult()
    
    print 'ALL DONE'

if __name__ == '__main__':
    main()
