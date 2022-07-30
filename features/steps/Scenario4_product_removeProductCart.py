from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql_get
from behave import given, when, then

import setup



@when('going to checkout')    
def validate_total_price(context):
    context.driver.find_element(By.ID, "shoppingCartLink").click()
    context.driver.find_element(By.XPATH, "//a[normalize-space()='REMOVE']").click()
    
@then('the cart should show "{empty_string}"')
def check_empty_cart(context, empty_string):
    empty_cart = context.driver.find_element(By.XPATH, "//label[@class='roboto-bold ng-scope']").text
    try:
        assert empty_cart == empty_string
    except Exception as e:
        raise ValueError("Is not empty!")


