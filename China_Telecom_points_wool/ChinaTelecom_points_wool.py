# encoding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys
import win32api
import win32con
from PIL import Image
import subprocess
import os
import re

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def depoint(img):   #input: gray image
    pixdata = img.load()
    w,h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pixdata[x,y-1] > 245:
                count = count + 1
            if pixdata[x,y+1] > 245:
                count = count + 1
            if pixdata[x-1,y] > 245:
                count = count + 1
            if pixdata[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x,y] = 255
    return img

def binarizing(img,threshold): #input: gray image
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


driver = webdriver.Chrome()
driver.get("http://js.189.cn/service/credit?in_cmpid=home-rfc-jfqd")
#driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath(xpath='/html/body/div[4]/div[1]/div/a[1]').click()
driver.find_element_by_xpath(xpath='//*[@id="logintPupup"]/a[1]').click()
time.sleep(2)
##用户名phonenumber
driver.find_element_by_xpath(xpath='//*[@id="cellphonePupup"]').send_keys('181*******')
##密码
driver.find_element_by_xpath(xpath='//*[@id="cellphoneloginformPupup"]/div[1]/input').send_keys('9*****')

qqq =driver.find_element_by_xpath('//*[@id="validateImage"]')
ActionChains(driver).context_click(qqq).perform()
win32api.keybd_event(86,0,0,0)  #v键位码是86
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
time.sleep(2)
if os.path.exists("C:\\my.jpg"):
    os.remove("C:\\my.jpg")
#下载jpg
subprocess.call('C:\Program Files\AutoIt3\demo_my\haha.exe')
time.sleep(1)
#识别图片
img = Image.open("C:\\my.jpg").convert("L")
print(img.format, img.size, img.mode)
img = binarizing(img, 140)
img = depoint(img)
img.save("C:\\mylast.jpg", 'JPEG')
time.sleep(2)
subprocess.call("C:\\Program Files\\Tesseract-OCR\\tesseract.exe C:\\mylast.jpg myresult --oem 3 --psm 7")
time.sleep(2)
#获取识别后验证码
f = open('myresult.txt', 'r')
mystr = f.read()
print(mystr.encode())
print(mystr)
time.sleep(1)
mystr = str(mystr)
print(mystr)
pat = '[0-9A-Za-z]'
res = re.findall(pat, mystr)
print(res)
mynewstr = ''.join(res)
print(mynewstr)
print(len(mynewstr))
if len(mynewstr)!=4:
    raise "error"

driver.find_element_by_xpath(xpath='//*[@id="cellphoneloginformPupup"]/p[2]/b/input').send_keys(mynewstr)
driver.find_element_by_xpath(xpath='//*[@id="cellphoneloginformPupupsubmitLoginBtn"]/span').click()
time.sleep(5)
driver.find_element_by_xpath(xpath='//*[@id="codeMsg"]').click()

time.sleep(60)
##登录操作
#email = raw_input('Email: ')
#password = raw_input('Password: ')
#pop3_server = raw_input('POP3 server: ')

email = 'myemail@163.com'
password = 'password'
pop3_server = 'pop.163.com'

server = poplib.POP3(pop3_server)
print(server.getwelcome())
server.user(email)
server.pass_(password)
resp, mails, octets = server.list()
##获取最新一封邮件的信息
resp, lines, octets = server.retr(len(mails))
print(type(lines))
print(lines)
msg_content = b' '.join(lines)
#msg = Parser().parsestr(msg_content)
#print(msg)
##匹配规则
kk = 'Subject: code=(\d\d\d\d\d\d)'
res = re.findall(kk, str(msg_content))
print(str(res))
server.quit()

vacode = ''
vacode = str(res)
print(vacode)
myvacode = vacode[2:8]
driver.find_element_by_xpath(xpath='//*[@id="randomPwdQDCX"]').send_keys(myvacode)
time.sleep(1)
driver.find_element_by_xpath(xpath='//*[@id="layout1QDCX"]/div[2]/div/div/dl/dd[4]/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath(xpath='//*[@id="js-just-qiandao"]/div').click()