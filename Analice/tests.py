# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path=r'C:\Users\Me\sel\geckodriver.exe')
driver.get('http://127.0.0.1:8000/')
head = driver.find_element_by_id('id_text_content')
head.send_keys('Locomia' + Keys.RETURN)
time.sleep(2)
head = driver.find_element_by_id('btn_reset').click()


driver = webdriver.Firefox(executable_path=r'C:\Users\Me\sel\geckodriver.exe')
driver.get('http://127.0.0.1:8000/')
head = driver.find_element_by_id('id_text_content')
head.send_keys('Locomia Locomia Locomia' + Keys.RETURN)
time.sleep(2)
head = driver.find_element_by_id('btn_execute').click()

#masthead-search-term