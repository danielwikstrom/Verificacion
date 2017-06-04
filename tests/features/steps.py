from lettuce import*
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

@step('the "([^"]*)" is empty')
def check_empty_text(step,textbox):
    # Create your tests here.
    assert world.driver.find_element_by_id(textbox).get_attribute('value') == ""

@step('"([^"]*)" is introduced in "([^"]*)"')
def write_feature(step,string,textbox):
    world.textBefore = world.driver.find_element_by_id(textbox).get_attribute('value')
    textAfter = world.textBefore+string
    textAfter = textAfter[0:200]

    world.driver.find_element_by_id(textbox).send_keys(textAfter)



    assert world.driver.find_element_by_id(textbox).get_attribute('value')== textAfter

@step('there is only "([^"]*)" in "([^"]*)"')
def check_only_text(step,string,textbox):
    assert world.driver.find_element_by_id(textbox).get_attribute('value')== string

@step('text in "([^"]*)" has not changed')
def not_changed(step,textbox):
    assert world.driver.find_element_by_id(textbox).get_attribute('value') == world.textBefore

@step('"([^"]*)" button is pressed')
def press_button(step,string):
    world.driver.find_element_by_id('btn_'+string).click()

@step('close Firefox')
def close(step):
    world.driver.close()

@step('is in result')
def result(step):
    time.sleep(2)
    assert str(world.driver.current_url[22:28]) == "result"
