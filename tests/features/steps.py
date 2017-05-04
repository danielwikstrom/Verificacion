from lettuce import*
from lettuce_webdriver.util import assert_false
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import TestCase

@step('Open firefox')
def open_firefox(step):
    world.driver = webdriver.Firefox()

@step('go to "([^"]*)"')
def go_to(step,string):
    world.driver.get(string)

@step('the text field is empty')
def check_empty_text(step):
    # Create your tests here.
    assert world.driver.find_element_by_id('id_text_content').get_attribute('value') == ""

@step('"([^"]*)" is introduced')
def write_feature(step,string):
    world.textBefore = world.driver.find_element_by_id('id_text_content').get_attribute('value')
    textAfter = world.textBefore+string
    textAfter = textAfter[0:100]

    world.driver.find_element_by_id('id_text_content').send_keys(textAfter)
    print world.driver.find_element_by_id('id_text_content').get_attribute('value')

    print textAfter
    assert world.driver.find_element_by_id('id_text_content').get_attribute('value')== textAfter

@step('there is only "([^"]*)" in text field')
def check_only_text(step,string):
    assert world.driver.find_element_by_id('id_text_content').get_attribute('value')== string

@step('text in text field has not changed')
def not_changed(step):
    assert world.driver.find_element_by_id('id_text_content').get_attribute('value') == world.textBefore

@step('"([^"]*)" button is pressed')
def press_button(step,string):
    world.driver.find_element_by_id('btn_'+string).click()

@step('close Firefox')
def close(step):
    world.driver.close()

@step('is in result')
def result(step):
    assert str(world.driver.current_url[22:28]) == "result"
