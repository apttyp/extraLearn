#coding:utf-8

import requests
import time
import re

def result():
    url1 = 'http://hq.sinajs.cn/?rn=1417610216083&list=AUDCHF,AUDHKD,AUDJPY,AUDUSD,CADHKD,CADJPY,CHFCAD,CHFHKD,DINIW,EURUSD,GBPEUR,GBPHKD,GBPUSD,USDCAD,USDCHF,USDCNY,USDHKD,USDJPY,gb_dji,gb_ixic,hf_C,hf_CAD,hf_CL,hf_GC,hf_S,hf_SI,int_hangseng,int_nikkei'
    url2 = 'http://hq.sinajs.cn/?rn=1417610565584&list=DINIW'
    url3 = 'http://hq2gjqh.eastmoney.com/em_futures2010numericapplication/index.aspx?type=f&id=CONC0&v=1417613016752&_=1417613016753'

    html1 = requests.get(url1)
    html2 = requests.get(url2)
    html3 = requests.get(url3)

    value1 = []
    value2 = []

    ISOTIMEFORMAT= '%Y-%m-%d %X'
    value1.append(time.strftime(ISOTIMEFORMAT,time.localtime()))
    value2.append(time.strftime(ISOTIMEFORMAT,time.localtime()))

    USDCNY = re.compile('var hq_str_USDCNY=".*?,(.*?),.*?";').findall(html1.text)
    DINIW = re.compile('".*?,(.*?),.*?";').findall(html2.text)
    CONC = re.compile('extendedFutures:\["0.00,0|0.00,0",".*?,(.*?),.*?"]').findall(html3.text)

    value1.append(USDCNY[0].encode('utf-8'))
    value1.append(DINIW[0].encode('utf-8'))
    #value2.append(CONC[1].encode('utf-8'))
   
    print value1
    print value2

if __name__=='__main__':
    result()
