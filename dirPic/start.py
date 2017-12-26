#-*- coding:utf-8 -*-
#__Date__    :  '2017-12-24'
#__Author__  :  'yapei.tang'

import os,sys,time
# from log import LOG,logger
import log
import requests
import datetime


# @logger('开始运行')
def main():

	nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	print nowtime
	con = requests.session()
	main_res = con.get('https://www.onejav.com')
	print main_res.text
	nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	print nowtime
	
if __name__ == '__main__':
	main()