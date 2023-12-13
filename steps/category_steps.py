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

@given("the user is logged in as an admin")
def log_in_as_admin(context):
    driver.get(URL)
    Functions.login_method_waiting(driver)


@step("the user is on the Categories page")
def go_to_categories_page(context):
    control_panel(driver, "categories")


@when('the user adds a new category with name "{category_name}" and slug "{category_slug}"')
def add_category(context, category_name, category_slug):
    # click "Add category" button
    add_category_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-list/form/div/a"))
    )
    add_category_button.click()
    # expand dropdown for parent id
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/div[1]/div/select"))
    )
    dropdown.click()
    # select parent id
    hammer_option = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/div[1]/div/select/option[5]"))
    )
    hammer_option.click()
    # write new category name in "name" field
    driver.find_element(
        By.ID, "name"
    ).send_keys(category_name)
    # write new category slug in "slug" field
    driver.find_element(
        By.ID, "slug"
    ).send_keys(category_slug)
    # click "Save" button
    driver.find_element(
        By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/button"
    ).click()


@then('the user should see a category add success message "{success_message}"')
def verify_added_successfully(context, success_message):
    # wait for save message
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/div"))
    )
    # assert the message is correct
    assert message.text == success_message
    # click "back" button
    driver.find_element(
        By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/a"
    ).click()
    time.sleep(3)

@step('the user deletes the category with name "{category_name}"')
def delete_category(context, category_name):
    # find created category by name
    search_bar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-list/form/div/input"))
    )
    search_bar.send_keys("new hammer category name")
    time.sleep(1)
    # click "Search" button
    driver.find_element(
        By.XPATH, "/html/body/app-root/div/app-list/form/div/button[1]"
    ).click()

    # delete newly created category
    time.sleep(2)
    delete_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/app-root/div/app-list/table/tbody/tr[1]/td[5]/button"))
    )
    delete_button.click()


@then('the user should see a category delete success message "{success_message}"')
def verify_deleted_successfully(context, success_message):
    delete_toast_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "body > app-root > app-toasts > ngb-toast"))
    ).text
    assert delete_toast_message == success_message
    time.sleep(3)
    driver.close()

