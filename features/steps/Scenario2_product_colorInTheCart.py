from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql_get
from behave import given, when, then

import setup



url = setup.default_url

specs = []


def store_db_notebook_data(data):
    global db_note_info
    db_note_info = data
def glb_variable():
    global product_on_website
    product_on_website =  {
        "PRODUCT_NAME": specs[0],
        "CUSTOMIZATION": specs[2],
        "DISPLAY": specs[3],
        "DISPLAY_RESOLUTION": specs[4],
        "DISPLAY_SIZE": specs[5],
        "MEMORY": specs[6],
        "OPERATING_SYSTEM": specs[7],
        "PROCESSOR": specs[8],
        "TOUCHSCREEN": specs[9],
        "WEIGHT": specs[10],
        "COLOR": specs[11],
        "PRICE": specs[1],
    }

@when('we are alredy on the page of the offer')   
def init_scenario(context): 
    context.driver = webdriver.Firefox(executable_path=setup.location)
    context.driver.implicitly_wait(30)

    
@when('collects more details from the product')
def getting_product_info_from_website(context):
    context.driver.get(url)
    WebDriverWait(context.driver,15).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='div-special-offer']//div//a")))
    go_to_offer = WebDriverWait(context.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='SPECIAL OFFER']")))
    context.driver.execute_script("arguments[0].click();", go_to_offer)
    see_offer = context.driver.find_element(By.XPATH, "//button[@id='see_offer_btn']")
    context.driver.execute_script("arguments[0].click();", see_offer)
    WebDriverWait(context.driver,15).until(EC.element_to_be_clickable((By.ID,"mainImg")))
    notebook_name = context.driver.find_element(By.XPATH, "//article[1]//div[@id='mobileDescription']//h1[@class='roboto-regular ng-binding']").get_attribute("innerHTML")
    notebook_price = context.driver.find_element(By.XPATH, "//article[1]//div[@id='mobileDescription']//h2[@class='roboto-thin ng-binding'][1]").get_attribute("innerHTML")
    notebook_color = context.driver.find_elements(By.XPATH, "//article[1]//*[starts-with(@id, 'product_')]//div[@id='Description']//div[@ng-show='!firstImageToShow']//span")
    notebook_price = stripping_value(char=notebook_price)
    specs.append(notebook_name.strip())
    specs.append(notebook_price)
    spec_list = context.driver.find_elements(By.XPATH, "//article[2]//div")
    for element in spec_list:
        spec_by = element.find_element(By.CLASS_NAME, "value").get_attribute("innerHTML")
        specs.append(spec_by)
    for element in notebook_color:
        if "colorSelected" in element.get_attribute("class"):
            specs.append(element.get_attribute("title"))
    glb_variable()

@when("Get color and more details from Database based on the notebooks name")  
def getting_product_info_from_database(context):
    result = mysql_get.db_notebooks(product_on_website["PRODUCT_NAME"]).get_all()
    store_db_notebook_data(result)

@when("select the color and add to the cart")
def select_color_add_cart(context):
    color = db_note_info["COLOR"]
    colors = context.driver.find_elements(By.XPATH, f"//article[1]//*[starts-with(@id, 'product_')]//div[@id='Description']//div[@ng-show='firstImageToShow']//span")
    for element in colors:
        if color in element.get_attribute("title"):
            element.click()
    context.driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART'][1]").click()

@then("The product is on the right color inside of the cart")
def make_sure_is_in_thecart(context):
    context.driver.find_element(By.ID, "shoppingCartLink").click()
    product_name_on_cart = context.driver.find_element(By.XPATH, "//table[@class='fixedTableEdgeCompatibility']//tbody//tr[@class='ng-scope']//td[2]").text
    color_of_the_product = context.driver.find_element(By.XPATH, "//table[@class='fixedTableEdgeCompatibility']//tbody//tr[@class='ng-scope']//td[4]//span")
    color_of_the_product = color_of_the_product.get_attribute('title')
    try:
        assert product_on_website["PRODUCT_NAME"] == product_name_on_cart.strip()
    except Exception as e:
        raise ValueError("The product on the cart was not the one selected to be added")
    try:
        assert db_note_info["COLOR"] == color_of_the_product.strip()
    except Exception as e:
        raise ValueError("the color selected is not the same on the cart")
    context.driver.close()

def stripping_value(char):
    char = char.split(" ")
    for i in char:
        if "$" in i:
            return float(i.strip().replace("R", "").replace("$", ""))
            


