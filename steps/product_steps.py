import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import Functions

URL = "https://practicesoftwaretesting.com/#/"
driver = webdriver.Chrome()


def control_panel(driver, button_name):
    admin_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'admin-menu'))
    )
    admin_menu.click()

    products_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/admin/' + button_name + '"]'))
    )
    products_menu.click()
    time.sleep(2)


#------------------------------#
#             GIVEN            #       
#------------------------------#

@given("the user is logged as an admin")
def go_to_products_panel(context):
    driver.get(URL)
    Functions.login_method_waiting(driver)

@given("the user is on the Products panel in the administrator's dashboard")
def go_to_products_panel(context):
    control_panel(driver, "products")


#------------------------------#
#             WHEN             #       
#------------------------------#

@when("the user selects a product to edit")
def select_product_to_edit(context):
    
    row_with_product = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]'))
    )

    context.product_name = row_with_product.find_element(By.XPATH, './td[2]').text
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test^="product-edit-"]'))
    ).click()

@when("edits the product details")
def edit_product_details(context):
    time.sleep(3)
    price_input = driver.find_element(By.ID, 'price')
    price_input.clear()
    price_input.send_keys(5)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-submit"]'))
    ).click()
    time.sleep(2)
    context.edit_completed_flag = driver.find_element(By.XPATH, '//div[@role="alert"]').text

@when("the user goes back to the product list")
def go_back_to_product_list(context):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-test="back"]'))
    ).click()

@when("the user searches for the edited product")
def search_for_edited_product(context):
    driver.find_element(By.XPATH, '//input[@data-test="product-search-query"]').send_keys(str(context.product_name))
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-search-submit"]'))
    ).click()


#------------------------------#
#             THEN             #       
#------------------------------#

@then("the updated product with the new data should appear in the product list")
def verify_updated_product_in_list(context):
    row_with_edited_product = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]'))
    )

    actual_price = row_with_edited_product.find_element(By.XPATH, './td[4]').text
    assert str(actual_price) == "$5.00", "Unexpected product price in the list"

@then("the browser is closed")
def close_browser(context):
    driver.close()
