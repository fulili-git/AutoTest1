#-*- coding=utf-8 -*-

from ddt import file_data
from selenium import webdriver
from page_object import login_page
@ddt
class Testlogin(login_page):
    @file_data('../data/user.yaml')
    def test_login(self):
        driver = webdriver.Chrome()
        lp = login_page(driver)
        lp.login(user,pwd)






