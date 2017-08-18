#coding:utf-8

import requests
import time
import re

def result():
    url = 'http://hq.sinajs.cn/rn=1502690925439list=fx_shkdcny'

    html = requests.get(url)

    value = []

    ISOTIMEFORMAT= '%Y-%m-%d %X'
    value.append(time.strftime(ISOTIMEFORMAT,time.localtime()))

    HKDCNY = re.compile('var hq_str_fx_shkdcny=".*?,(.*?),.*?";').findall(html.text)

    print HKDCNY
    value.append(HKDCNY[0].encode('utf-8'))
    print value   

if __name__=='__main__':
    result()
