import requests
import sys
import re

url = 'http://wx.yingtaoyun.cn/tlhz/mpv2/photov2/show/47423.html?from=singlemessage&isappinstalled=0'

def run_main():
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; Chitanda/Akari) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/6.0.0.58_r884092.501 NetType/WIFI'
    }
    r = requests.get(url, headers=header)
    print r.headers
    mm=r.text
    print mm

if __name__=='__main__':
	run_main()