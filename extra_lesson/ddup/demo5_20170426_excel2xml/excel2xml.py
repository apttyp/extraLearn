#!/usr/bin/env python
#coding:utf-8

import io
import xlrd
from lxml import etree
import json

excel1 = 'city.xls'

def readxls():
    data = {}
#start a xlrd object
    book = xlrd.open_workbook(excel1)
#select a working sheet
    sheet = book.sheet_by_name('city')
#from sheet get row and col
    # rows = sheet.nrows
    # cols = sheet.ncols
#put data into a dict
    # for i in range(rows):
    for i in range(sheet.nrows):
        data[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)

    print data
    print json.dumps(data)
    print json.dumps(data, ensure_ascii = False)
    return json.dumps(data, ensure_ascii = False)

def toxml(data):
#Create a document and elements
    root = etree.Element('root')
    stu = etree.SubElement(root, 'city')
# Create a comment
    stu.append(etree.Comment(u' 城市信息\t'))
# Create a text
    stu.text = data
# Save to file
    tree = etree.ElementTree(root)
    tree.write('city.xml', encoding='utf-8', pretty_print=True, xml_declaration=True)

if __name__ == '__main__':
	data = readxls()
	toxml(data)