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

        # add brands
        self.add_brand(driver)

        # Loop through each row to find the element with the specified Slug and Name
        # Find the table rows
        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr'))
        )

        # Flag to check if the element is found
        element_found = False

        # Loop through each row to check for Slug and Brand Name
        for row in table_rows:
            # Extract Slug and Brand Name values from each row
            slug = row.find_element(By.XPATH, './td[3]').text
            brand_name = row.find_element(By.XPATH, './td[2]').text

            # Check if Slug and Brand Name match the desired values
            if slug == "testing" and brand_name == "testing":
                element_found = True
                break

        # Assert if the element is found in the table based on Slug and Brand Name
        assert element_found, "Element with Slug 'abc' and Brand Name 'xyz' not found in the table"

    # case 03-001
    def test_delete_brand(self):
        # setup
        driver = self.set_up()

        # click BRANDS button
        click_brands(driver)

        # adding brands
        self.add_brand(driver)

        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr'))
        )

        found_element = None
        for row in table_rows:
            slug = row.find_element(By.XPATH, './td[3]').text
            name = row.find_element(By.XPATH, './td[2]').text
            serial = row.find_element(By.XPATH, './td[1]').text

            # Check if Slug and Name match the desired values
            if slug == "testing" and name == "testing":
                found_element = row
                # Click the delete button and break the loop
                delete_button = row.find_element(By.XPATH, f'./td[4]//button[@data-test="brand-{serial}-delete"]')
                delete_button.click()
                break

        assert found_element is not None, "Element with Slug 'test' and Name 'test' deleted"

    @staticmethod
    def add_brand(driver):
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

    # case 04-001
    def test_update_brand(self):
        # setup
        driver = self.set_up()

        click_brands(driver)

        self.add_brand(driver)

        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr'))
        )

        for row in table_rows:
            slug = row.find_element(By.XPATH, './td[3]').text
            name = row.find_element(By.XPATH, './td[2]').text
            serial = row.find_element(By.XPATH, './td[1]').text
            if slug == "testing" and name == "testing":
                edit_button = row.find_element(
                    By.XPATH, f'//a[contains(@data-test, "brand-{serial}-edit")][contains(@href, "edit/{serial}")]'
                )
                edit_button.click()
                break

        # Find and fill the "Name" and "Slug" input fields
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-test="name"]'))
        )
        slug_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-test="slug"]'))
        )

        # Clear existing values and input new values for Name and Slug
        name_input.clear()
        name_input.send_keys("testing2")
        slug_input.clear()
        slug_input.send_keys("testing2")

        # Find and click the "Save" button
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test="brand-submit"]'))
        )
        save_button.click()

        # Find and click the "Back" button
        back_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@data-test="back"]'))
        )
        back_button.click()

        found_element = None
        for row in table_rows:
            slug = row.find_element(By.XPATH, './td[3]').text
            name = row.find_element(By.XPATH, './td[2]').text
            serial = row.find_element(By.XPATH, './td[1]').text

            # Check if Slug and Name match the desired values
            if slug == "testing2" and name == "testing2":
                found_element = row
                # Click the delete button and break the loop
                delete_button = row.find_element(By.XPATH, f'./td[4]//button[@data-test="brand-{serial}-delete"]')
                delete_button.click()
                break

        assert found_element is not None, "Element with Slug 'test' and Name 'test' deleted"

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
