from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Functions():
    def login_method(driver):
        sign_in_button = driver.find_element(By.XPATH, '//a[@data-test="nav-sign-in"]')
        sign_in_button.click()

        email_field = driver.find_element(By.ID, 'email')
        email_field.send_keys('admin@practicesoftwaretesting.com')

        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('welcome01')

        login_button = driver.find_element(By.XPATH, '//input[@data-test="login-submit"]')
        login_button.click()
        time.sleep(2)

    def login_method_waiting(driver):
        try:
            navigation_button = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-header/nav/div/button/span'))
            )
            navigation_button.click()
        except TimeoutException:
            print("")

        time.sleep(1)

        sign_in_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-test="nav-sign-in"]'))
        )
        sign_in_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )
        email_field.send_keys('admin@practicesoftwaretesting.com')

        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        )
        password_field.send_keys('welcome01')

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@data-test="login-submit"]'))
        )
        login_button.click()

    def control_panel(self, driver, button_name):
        # Available button_name:
            # dashboard, brands, categories, products, orders, users, messages, settings
        admin_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'admin-menu'))
        )
        admin_menu.click()

        products_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@routerlink="/admin/' + button_name + '"]'))
        )
        products_menu.click()
        time.sleep(2)