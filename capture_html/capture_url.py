# 获取特定页面的url
from urllib2 import urlopen
import re
p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('http://www.6789.com/').read()
for url, name in p.findall(text):
    print '%s (%s)' % (name, url)