#-*- coding=utf-8 -*-

from selenium import webdriver
import time

class BasePage:
    def __int__(self,driver):
        #self.driver = webdriver.Chrome()
        self.driver  = driver

    #访问网页url
    def  visit(self,url):
        self.driver.get(url)

    #元素定位
    def locator(self,loc):
        self.driver.find_element(*loc)

    #元素输入
    def input(self,loc,txt):
        self.locator(loc).send_keys(txt)
    #点击元素
    def click(self,loc):
        self.locator(loc).click()

    #等待时间
    def wait(self,time1):
        time.sleep(time1)

    #关闭浏览器
    def quit(self):
        self.driver.quit()
