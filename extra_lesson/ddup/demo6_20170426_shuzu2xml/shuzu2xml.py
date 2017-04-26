#!/usr/bin/env python
#coding:utf-8

import io
import xlrd
from lxml import etree
import json

excel1 = 'number.xls'

def readxls():
    data = []
#start a xlrd object
    book = xlrd.open_workbook(excel1)
#select a working sheet
    sheet = book.sheet_by_name('haha')
#from sheet get row and col
    rows = sheet.nrows
    cols = sheet.ncols
    temp = []
#put data into a dict
    # for i in range(rows):
    for i in range(rows):
        for j in range(cols):
            temp.append(sheet.cell_value(i, j))
        # data[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)
        data.append(temp)
        temp = []
    return json.dumps(data, encoding='utf-8', ensure_ascii = False)

def toxml(data):
#Create a document and elements
    root = etree.Element('root')
    stu = etree.SubElement(root, 'number')
# Create a comment
    stu.append(etree.Comment(u' 数字信息\t'))
# Create a text
    stu.text = data
# Save to file
    tree = etree.ElementTree(root)
    tree.write('number.xml', encoding='utf-8', pretty_print=True, xml_declaration=True)

if __name__ == '__main__':
	data = readxls()
	toxml(data)