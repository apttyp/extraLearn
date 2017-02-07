# encoding: UTF-8
#Blackboardfirst lesson
import requests
import re
url = 'http://www.heibanke.com/lesson/crawler_ex00/'
r = requests.get(url)
res = r.text
p = re.compile('<h3>.*</h3>')
for content in p.findall(res):
    print content
    print content.__class__
    mm = re.findall(r"\d\d\d\d\d", content)
    print mm.__str__()
    num = "".join(mm)
    tmpurl = url + num
    print tmpurl
x = 1
while x <= 20:
    print x
    x = x + 1
    r = requests.get(tmpurl)
    res = r.text
    p = re.compile('<h3>.*</h3>')
    for content in p.findall(res):
        print content
        print content.__class__
        mm = re.findall(r"\d\d\d\d\d", content)
        print mm.__str__()
        num = "".join(mm)
        tmpurl = url+num
        print tmpurl