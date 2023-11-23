from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


class Test(TestCase):
    func = Functions()
    URL = "https://practicesoftwaretesting.com/#/"

    def set_up(self):
        driver = webdriver.Chrome()
        driver.get(self.URL)
        Functions.login_method_waiting(driver)
        return driver

    # case 01-001
    def test_display_brands(self):
        # setup
        driver = self.set_up()

        # click BRANDS button
        click_brands(driver)

        # test visibility of brands
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'table-hover'))
        )

        # check if the "Id," "Name," and "Slug" headers are present
        headers = table.find_elements(By.TAG_NAME, 'th')
        header_texts = [header.text for header in headers]

        assert "Id" in header_texts, "'Id' column not found"
        assert "Name" in header_texts, "'Name' column not found"
        assert "Slug" in header_texts, "'Slug' column not found"

        # Check if there are rows in the table
        rows = table.find_elements(By.TAG_NAME, 'tr')
        assert len(rows) > 0, "Table has no rows"

    # case 02-001
    def test_add_brand(self):
        # setup
        driver = self.set_up()

        # click BRANDS button
        click_brands(driver)

        # click ADD BRAND button

        # fill in the date

        # click SAVE button

        # click BACK button

        # check the list of brands

    # case 03-001
    def test_delete_brand(self):
        # setup
        driver = self.set_up()

        # click BRANDS button

        # click EDIT button

        # edit fields

        # click SAVE button

        # click BACK button

        # check the list of BRANDS

    # case 04-001
    def test_update_brand(self):
        # setup
        driver = self.set_up()

        # click BRANDS button

        # click DELETE button

        # check the list of BRANDS

    # case 05-001
    def test_5(self):
        self.fail()

    # case 06-001
    def test_6(self):
        self.fail()

    # case 07-001
    def test_7(self):
        self.fail()

    # case 07-002
    def test_7_2(self):
        self.fail()

    # case 08-001
    def test_8(self):
        self.fail()

    # case 09-001
    def test_9(self):
        self.fail()

    # case 10-001
    def test_10(self):
        self.fail()
