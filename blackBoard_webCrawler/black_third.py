#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
website1 = 'http://www.heibanke.com/accounts/login'
website2 = 'http://www.heibanke.com/lesson/crawler_ex02/'

wrongNotify = '错误'
res1 = requests.get(website1)     # 访问登录页面获取登录要用的csrftoken
cookies1 = res1.cookies
print cookies1
token1 = cookies1['csrftoken']      # 保存csrftoken
# 将csrftoekn存入字段csrfmiddlewaretoken
dataWebsite1 = {'username': 'ppq123','password': '123456','csrfmiddlewaretoken': token1}
res2 = requests.post(website1, data=dataWebsite1, cookies=cookies1, allow_redirects=False)
cookies2 = res2.cookies
token2 = cookies2['csrftoken']

for pwd in range(1,31):
    # 以下步骤原理和上面一样
    dataWebsite2 = {'username': 'ppq123', 'password': pwd, 'csrfmiddlewaretoken': token2}
    result = requests.post(website2, data=dataWebsite2, cookies=cookies2)
    if wrongNotify in result.text:
        print '密码%d错误' % pwd
        pwd += 1
    else:
        print '密码是%d' % pwd
        print result.text
        break
