#!/usr/bin/env python
import json
import xlwt

file1 = 'number.txt'
excel1 = 'myexcel.xls'
def toexcel():
	data = get_json(file1)
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet('haha')
	print data
	row = len(data)
	col = len(data[0])
	print row
	print col
	
	for i in range(row):
		for j in range(col):
			sheet.write(i,j,data[i][j])
	workbook.save(excel1)

def get_json(file1):
    with open(file1, 'r') as f:
        #The codec should be the same as the file encoding.
        text = f.read().decode('utf-8')
        return json.loads(text)

if __name__=='__main__':
	toexcel()

