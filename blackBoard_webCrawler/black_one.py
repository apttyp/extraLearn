# encoding: UTF-8
#Blackboardfirst lesson
import requests
import re
url = 'http://www.heibanke.com/lesson/crawler_ex00/'

r = requests.get(url)
# print r.text
res = r.text
# print res
p = re.compile('<h3>.*</h3>')
for content in p.findall(res):
    print content
