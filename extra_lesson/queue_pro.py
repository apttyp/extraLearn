from multiprocessing import Process,Queue
import os,time,random

def write(p):
	for value in ['a','b','c']:
		print 'Put %s to queue...' %value
		p.put(value)
		time.sleep(random.random())

def read(p):
	while True:
		value = p.get()
		print 'Get %s from queue.' %value
		time.sleep(random.random())

if __name__ == '__main__':
	p = Queue()
	pw = Process(target=write,args=(p,))
	pr = Process(target=read,args=(p,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
