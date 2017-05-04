from lettuce import*
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import TestCase

driver = webdriver.Firefox(executable_path=r'C:\Users\Me\sel\geckodriver.exe')


@step('there is (\c+) in the text field')
def check_text(step, string):
    # Create your tests here.
    driver.get('http://127.0.0.1:8000/')
    driver.find_element_by_id('id_text_content').send_keys('Locomia' + Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_id('btn_reset').click()

@step('(\c+) button is pressed')
def reset_with_text(step,string):
    driver.find_element_by_id('+string+').click()

@step('a warning message appears')
def reset_with_text(step):
    ###asert
