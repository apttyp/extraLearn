#-*-coding:utf-8 -*-
import requests,json
from lxml import etree

#get execution
myurl1 = 'https://account.dui.ai/cas/login'
s = requests.Session();
r = s.get(myurl1)
mm=r.text
page = etree.HTML(mm)
hrefs = page.xpath(u'//*[@id="form"]/input[1]')
myres = ""
for href in hrefs:
    myres = href.attrib['value']

print(s.headers)
#post to login
payload = {'username':'*****', 'password':'******', 'execution':myres, '_eventId':'submit'}
mytt = s.post(url=myurl1,data=payload)
print(s.headers)

#skill to show
skillId = '100000296'
myques = '1000加一等于几'
gmurl = 'https://www.dui.ai/console/skills/api/v1.0/skills/'+skillId+'/parse?sentence='+myques
print(gmurl)

res = s.get(gmurl)
result = res.text
# print(result)
ggres = json.loads(result)
print(ggres)
item = ggres["result"]["dlg"]
# print(item[0]["dm"]["task"])
# print(item[0]["dm"]["intentName"])
print(item[0]["dm"]["nlg"])
