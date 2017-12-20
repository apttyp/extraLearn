#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re
import sys
import time
import threading

reload(sys)
sys.setdefaultencoding('utf8')

def auto_log():
    global cookies2
    global token2
    res1 = requests.get(website1)     # 访问登录页面获取登录要用的csrftoken
    cookies1 = res1.cookies
    token1 = cookies1['csrftoken']      # 保存csrftoken
# 将csrftoekn存入字段csrfmiddlewaretoken
    dataWebsite1 = {'username': 'ppq123','password': '123456','csrfmiddlewaretoken': token1}
    res2 = requests.post(website1, data=dataWebsite1, cookies=cookies1, allow_redirects=False)
    print res2.text
    cookies2 = res2.cookies
    token2 = cookies2['csrftoken']
    #return token2,cookies2

def get_pass(cookie2,token2):
    global password
    n = 1
    while n>0:
        if len(password)==100:
	    break
        else:
	    dataWebsite2 = {'username': 'ppq123', 'password': '123456', 'csrfmiddlewaretoken': token2}
	    res = requests.post(listurl, data=dataWebsite2, cookies=cookies2)
	    res_text = res.text
	    p1 = re.compile('password_pos">(.*)</td>')
	    p2 = re.compile('password_val">(.*)</td>')
	    mypos = []
	    myval = []
	    for data in p1.findall(res_text):
	        mypos.append(data)
	    for data in p2.findall(res_text):
	        myval.append(data)
	    for i in range(5):
	        password[mypos[i]] = myval[i]
	print password
    #return password

def sortedDictKey(adict):
	keys = adict.keys()
	keys.sort() 
	return map(adict.get,keys)

def int_sort_dict(mydict):
	tmp = []
	for i in range(100):
	    tmp.append(0);
	for item in mydict:
	    print int(item)
	    print mydict[item]
	    tmp[int(item)-1] = mydict[item]
	    
	return tmp
	

def login_new():
    global password
    global mylist
    mystr = ""
    while True:
    	print 'METHOD login_new()'
	if len(password)==100:
	    mylist=int_sort_dict(password)
 	    #sorted(password.iteritems(), key=lambda asd:asd[0], reverse = False)
	    #password = sorted(password.items(), key=lambda e:e[0], reverse=False)
	    print "mylist"
	    print mylist
	    print "str mylist"
	    mystr = ''.join(mylist)
	    #for i in range(100):
		#mystr = mystr.join(mylist[i])
	    print mystr
	    #mystr = str(mylist)
	    #print mystr
            dataWebsite3 = {'username': 'ppq123', 'password': mystr, 'csrfmiddlewaretoken': token2}
            last = requests.post(URL, data=dataWebsite3, cookies = cookies2)
            print last.text
	    break 
	else:
	    time.sleep(2)

def main():
    #threads = []
    for i in range(30):
	th = threading.Thread(target=get_pass(cookies2, token2))
	#threads.append(th)
	th.start()
	th.join()
    
#    for i in range(6):
#	threads[i].start()
#
#    for i in range(6):
#	threads[i].join()

if __name__ == '__main__':
    website1 = 'http://www.heibanke.com/accounts/login'
    URL = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex03/'
    listurl = 'http://www.heibanke.com/lesson/crawler_ex03/pw_list/'
    wrongNotify = '错误'
    password = {}
    auto_log()
    main()
    login_new()
