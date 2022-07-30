from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import mysql_get
from behave import given, when, then
from time import sleep

import setup



url = setup.default_url
db_note_info = dict
product_on_website = { 
        "PRODUCT_NAME": str,
        "COLOR": str,
        "PRICE": float,
        "TOTAL_PRICE": float,
        "AMOUNT": int
}


@when('on the main page')   
def init_scenario(context): 
    context.driver = webdriver.Firefox(executable_path=setup.location)
    context.driver.implicitly_wait(30)

def retry_click_element(context, element, mode=0):
    retry=5
    for retries in range(retry):
        try:
            if mode == 0:
                context.driver.find_element(By.XPATH, element).click()
            else:
                element.click()
            return
        except Exception:
            if retries >= retry:
                raise ValueError(f"Not able to click on element: {element}")
            sleep(1)
            pass

def getting_product_info_from_database(context, productName):
    global db_note_info
    result = mysql_get.db_notebooks(productName).get_all()
    db_note_info = result

@when('look from the "{productName}" on the search box')
def getting_product_info_from_website(context, productName):
    getting_product_info_from_database(context, productName)
    context.driver.get(url)
    context.driver.find_element(By.XPATH, "//a[@title='SEARCH']").click()
    context.driver.find_element(By.XPATH, "//input[@id='autoComplete']").send_keys(productName)
    context.driver.find_element(By.XPATH, "//input[@id='autoComplete']").send_keys(Keys.ENTER)
    product_list = context.driver.find_elements(By.XPATH, "  //div[@class='cell categoryRight']//ul")
    for products in product_list:
        product_name = products.text.upper().strip().split("\n")
        if product_name[0] == productName:
            product_on_website["PRODUCT_NAME"] = productName
            price = float(product_name[1].replace("R", "").replace("$", ""))
            product_on_website["PRICE"] = price
            retry_click_element(context,element="//div[@data-ng-click='closeSearchForce()']")
            context.driver.find_element(By.XPATH, "(//li[@ng-repeat='product in [] | productsFilterForCategoriesProduct:searchResult:minPriceToFilter:maxPriceToFilter:productsInclude'])[1]").click()

@when('changing the color to "{color}"')
def select_color_add_cart(context, color):
    new_color = color
    product_on_website["COLOR"] = color
    colors = context.driver.find_elements(By.XPATH, f"//article[1]//*[starts-with(@id, 'product_')]//div[@id='Description']//div[@ng-show='firstImageToShow']//span")
    for element in colors:
        if new_color in element.get_attribute("title"):
            retry_click_element(context, element, mode=1)

@when('Add "{amount}" products and add to the cart')
def increase_amount_add_cart(context, amount):
    product_on_website["AMOUNT"] = int(amount)
    for qty in range(1, int(amount)):
        context.driver.find_element(By.XPATH, "//div[@class='plus']").click()
    context.driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART'][1]").click()
    

@when('Access the checkout and validate the sum of the product and compare to the sum of the website')    
def validate_total_price(context):
    context.driver.find_element(By.ID, "shoppingCartLink").click()
    context.driver.find_element(By.ID, "checkOutButton").click()
    total_price = context.driver.find_element(By.XPATH, "//span[@class='roboto-medium totalValue ng-binding']").text
    product_on_website["TOTAL_PRICE"] = float(total_price.strip().replace("R", "").replace("$", "").replace(",", ""))
    try:
        assert product_on_website["TOTAL_PRICE"] == (product_on_website["AMOUNT"] * product_on_website["PRICE"])
    except Exception as e:
        raise ValueError("The amount * price of all products are not the same as the total on the website")

@then('update the database with the color used on the product "{productName}" in the website')    
def update_color_database(context, productName):
    global product_on_website, db_note_info
    mysql_get.db_notebooks().update_values(ID=mysql_get.db_notebooks().get_id(), Column="COLOR", Value=product_on_website["COLOR"])
    getting_product_info_from_database(context, productName)
    try:
        assert product_on_website["COLOR"] == db_note_info["COLOR"]
    except Exception as e:
        raise ValueError("The updated color is not the same on the database")
    context.driver.close()

def stripping_value(char):
    char = char.split(" ")
    for i in char:
        if "$" in i:
            return float(i.strip().replace("R", "").replace("$", ""))
            


