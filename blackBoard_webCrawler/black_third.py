# # encoding: UTF-8
# #Blackboardsecond lesson
# import requests
# #avoid UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 108: ordinal not in range(128)
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# s = requests.Session()
# url = 'http://www.heibanke.com/accounts/login'
# re = s.get(url)
# print re.cookies
# print re.cookies['csrftoken']
# mm=re.cookies['csrftoken']
# print re.headers
# payload = {'username': 'haha22haha', 'password': '1183930855'}
# # print payload
# headers = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "Content-Encoding": "gzip, deflate",
#     "Transfer-Encoding": "chunked",
#     "Accept-Language":"zh-CN,zh;q=0.8",
#     "Content-Type":"application/x-www-form-urlencoded",
#     "Cookie":"csrftoken=" + mm,
#     "Host":"www.heibanke.com",
#     "Origin":"http://www.heibanke.com",
#     "Referer":"http://www.heibanke.com/accounts/login",
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }
# r = s.post(url, data=payload, headers=headers)
# res = r.text
# print res


# coding=utf-8
import requests

website1 = 'http://www.heibanke.com/accounts/login'
website2 = 'http://www.heibanke.com/lesson/crawler_ex02'
wrongNotify = '您输入的密码错误, 请重新输入'

s = requests.Session()
s.get(website1)     # 访问登录页面获取登录要用的csrftoken
token1 = s.cookies['csrftoken']      # 保存csrftoken
print token1
# 将csrftoekn存入字段csrfmiddlewaretoken
dataWebsite1 = {'username': 'user',
                'password': 'password',
                'csrfmiddlewaretoken': token1
                }
s.post(website1, data=dataWebsite1)
pwd = 1
while pwd < 30:
    # 以下步骤原理和上面一样
    s.post(website2)
    token2 = s.cookies['csrftoken']
    dataWebsite2 = {'username': 'haha22haha',
                'password': pwd,
                'csrfmiddlewaretoken': token2
                }
    result = s.post(website2, data=dataWebsite2)

    if wrongNotify in result.content:
        print '密码%d错误' % pwd
        pwd += 1
    else:
        print '密码是%d' % pwd
        print result.content
        break