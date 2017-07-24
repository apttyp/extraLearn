#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(level=logging.DEBUG)

options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://www.baidu.com')
time.sleep(5)
print driver.find_element_by_xpath('//*[@id="main-message"]/div[2]').text()
#driver.find_element_by_xpath('//*[@id="main-content"]').send_keys(Keys.SPACE)
time.sleep(3)
#driver.find_element_by_xpath('//*[@id="main-content"]').send_keys(Keys.SPACE)

#driver.get("http://www.youdao.com")
#driver.find_element_by_name("q").send_keys("hello")
#driver.find_element_by_name("q").send_keys("key.ENTER")
#driver.close()
