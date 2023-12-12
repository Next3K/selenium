from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from functions import Functions


@staticmethod
def click_brands(driver):
    # click BRANDS button
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'admin-menu'))
    )
    dropdown.click()

    brands_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-test="nav-admin-brands"]'))
    )
    brands_button.click()


@staticmethod
def func_add_brand(driver):
    # Wait for the "Add Brand" button to be clickable using XPath
    add_brand_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-test="brand-add"]'))
    )
    # Click the "Add Brand" button
    add_brand_button.click()
    # Locate the "Name" and "Slug" input fields and the "Save" button using XPath
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-test="name"]'))
    )
    slug_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@data-test="slug"]'))
    )
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="brand-submit"]'))
    )
    back_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-test="back"]'))
    )
    # Fill in the "Name" and "Slug" fields
    name_input.send_keys("testing")
    slug_input.send_keys("testing")
    # Click the "Save" button
    save_button.click()
    # Click the "Back" button after saving
    back_button.click()


URL = "https://practicesoftwaretesting.com/#/"
driver = webdriver.Chrome()


@given("the user is on the Brands page")
def go_to_brands_page(context):
    driver.get(URL)
    Functions.login_method_waiting(driver)
    click_brands(driver)


@when('the user adds a brand with Slug "{slug}" and Name "{name}"')
def add_brand(context, slug, name):
    func_add_brand(driver)


@then('the brand with Slug "{slug}" and Name "{name}" should appear in the brands table')
def verify_brand_appears(context, slug, name):
    table_rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr'))
    )

    element_found = False
    for row in table_rows:
        row_slug = row.find_element(By.XPATH, './td[3]').text
        row_brand_name = row.find_element(By.XPATH, './td[2]').text

        if row_slug == slug and row_brand_name == name:
            element_found = True
            break

    assert element_found, f"Element with Slug '{slug}' and Brand Name '{name}' not found in the table"

    driver.close()
