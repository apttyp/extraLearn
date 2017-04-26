#!/usr/bin/env python
#coding:utf-8

import io
import xlrd
from lxml import etree
import json

excel1 = 'student.xls'

def readxls():
	kv = []
	data = {}
#start a xlrd object
	book = xlrd.open_workbook(excel1)
#select a working sheet
	sheet = book.sheet_by_name('student')
#from sheet get row and col
	rows = sheet.nrows
	cols = sheet.ncols
#put data into a dict
	for i in range(rows):
		for j in range(1,cols):
			if type(sheet.cell_value(i,j)) == float:
				kv.append(int(sheet.cell_value(i, j)))
			else:
				kv.append(sheet.cell_value(i,j))
		data[str(int(sheet.cell_value(i, 0)))] = kv
		kv=[]
	print data
	print json.dumps(data)
	print json.dumps(data, ensure_ascii = False)
	return json.dumps(data, ensure_ascii = False)

def toxml(data):
#Create a document and elements
    root = etree.Element('root')
    stu = etree.SubElement(root, 'student')
# Create a comment
    stu.append(etree.Comment(u' 学生信息表\n\t"id" : [名字, 数学, 语文, 英文]'))
# Create a text
    stu.text = data
# Save to file
    tree = etree.ElementTree(root)
    tree.write('student3.xml', encoding='utf-8', pretty_print=True, xml_declaration=True)

if __name__ == '__main__':
	data = readxml()
	toxml(data)