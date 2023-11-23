from selenium import webdriver
from selenium.webdriver.common.by import By  # Dodaj import dla klasy By
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

    def product_control_panel(driver):
        admin_menu = driver.find_element(By.ID, 'admin-menu')
        admin_menu.click()
        time.sleep(2)

        products_menu = driver.find_element(By.XPATH, '//a[@routerlink="/admin/products"]')
        products_menu.click()
        time.sleep(2)

    
