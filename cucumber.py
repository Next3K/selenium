from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


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


@given("the user is on the Brands page")
def go_to_brands_page(context):
    context.driver = context.set_up()
    click_brands(context.driver)


@when('the user adds a brand with Slug "{slug}" and Name "{name}"')
def add_brand(context, slug, name):
    context.add_brand(context.driver, slug, name)


@then('the brand with Slug "{slug}" and Name "{name}" should appear in the brands table')
def verify_brand_appears(context, slug, name):
    table_rows = WebDriverWait(context.driver, 10).until(
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

    context.driver.close()
