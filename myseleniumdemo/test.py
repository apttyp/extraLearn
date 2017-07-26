#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import logging

#logging.basicConfig(level=logging.DEBUG)

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://www.baidu.com')
time.sleep(5)
print driver.find_element_by_xpath('//*[@id="lg"]')
time.sleep(3)
for image in driver.find_elements_by_tag_name("img"):
    print (image.text)
    print (image.size)
    print (image.tag_name)
