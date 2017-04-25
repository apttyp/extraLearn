#!/usr/bin/env python
import json
import xlwt
import xlrd

testfile = 'file1'
sheetname = 'city'
excel = 'myexcel.xls'

def json2excel():
#demo1
#	f = open('file1','r')
#	text = f.read().decode('utf-8')
#	setting = json.loads(text)
#	print setting

#demo2
#	st = ''
#	with open(testfile) as f:
#		print f
#		for line in f.readlines():
#			st+=line
#		data = json.loads(st)
#		print data
#Get json data
	info = get_json(testfile)
#Create excel object
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet(sheetname)
#Cal row and coloum
	row = len(info)
	col = len(info[str(1)])

#write num
	for i in range(row):
		sheet.write(i,0,i+1)
#write data
	for i in range(row):
		for j in range(col):
			val = info[str(i+1)]
			sheet.write(i,j+1,val)
	workbook.save(excel)

#with open('file1', 'r') as f:
#    	#print f.read()
#	for line in f.readlines():
#		print line

def get_json(testfile):
    with open(testfile, 'r') as f:
        #The codec should be the same as the file encoding.
        text = f.read().decode('utf-8')
        return json.loads(text)

if __name__=='__main__':
	json2excel()
