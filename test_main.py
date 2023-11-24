import os
import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functions import Functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import unittest

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
    URL = "https://practicesoftwaretesting.com/#/"
    func = Functions()

    def set_up(self):
        driver = webdriver.Firefox()
        driver.get(self.URL)
        Functions.login_method_waiting(driver)
        return driver
    
    def set_up_without_login(self):
        driver = webdriver.Firefox()
        driver.get(self.URL)
        return driver

    #case 01-001
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
        driver.close()

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
        driver.close()

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
        driver.close()

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
        time.sleep(1)
        name_input.click()
        name_input.clear()
        name_input.send_keys("testing2")
        time.sleep(1)
        slug_input.click()
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

        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr'))
        )

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
        driver.close()

    # # case 05-001
    def test_update_product(self):
        try:
            #--SETUP
            driver = self.set_up()
        
            #--GO TO PRODUCT PANEL
            self.func.control_panel(driver, "products")
        
            #--SELECT PRODUCT
            row_with_product =  WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]'))
            )

            #--get product name for verify
            product_name = row_with_product.find_element(By.XPATH, './td[2]').text
        
            #--CLICK EDIT BUTTON
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test^="product-edit-"]'))
            ).click()
        
            #--EDIT PRODUCT DETAILS
            time.sleep(3)
            price_input = driver.find_element(By.ID, 'price')
            price_input.clear()
            price_input.send_keys(5)
        
            #--SAVE PRODUCT DETAILS
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-submit"]'))
            ).click()

            #--get status info for verify
            time.sleep(2)
            edit_completed_flag = driver.find_element(By.XPATH, '//div[@role="alert"]').text
        
            #--BACK TO PRODUCT LIST
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@data-test="back"]'))
            ).click()
        

            #--GET DATA FOR ASSERTS
            driver.find_element(By.XPATH, '//input[@data-test="product-search-query"]').send_keys(str(product_name))
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-search-submit"]'))
            ).click()

            row_with_edited_product =  WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, '//tbody/tr[1]'))
            )
        
            actual_price = row_with_edited_product.find_element(By.XPATH, './td[4]').text

            #--ASSERTS
            self.assertEqual(str(actual_price), "$5.00")
            self.assertEqual(str(edit_completed_flag), "Product saved!")
        finally:
            driver.close()     

    # case 06-001
    def test_add_product_with_wrong_data(self):
        try:
            #--SETUP
            driver = self.set_up()
        
            #--GO TO PRODUCT PANEL
            self.func.control_panel(driver, "products")
            time.sleep(2)

            #--ADD PRODUCT
            add_product_button = driver.find_element(By.XPATH, '//a[@data-test="product-add"]')
            add_product_button.click()
            time.sleep(1)

            #--TRY TO SAVE PRODUCT WITHOUT DATA
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-submit"]'))
            ).click()
            time.sleep(2)

            #--ASSERTS
            alerts_xpath = "/html/body/app-root/div/app-products-add-edit/div/form/div[2]/div[1]"
            self.assertEqual(driver.find_element(By.XPATH, f"{alerts_xpath}/div[1]/div[2]/div").text,"Name is required")
            self.assertEqual(driver.find_element(By.XPATH, f"{alerts_xpath}/div[2]/div[2]/div").text,"Description is required")
            self.assertEqual(driver.find_element(By.XPATH, f"{alerts_xpath}/div[3]/div[2]/div").text,"Quantity is required")
            self.assertEqual(driver.find_element(By.XPATH, f"{alerts_xpath}/div[4]/div[2]/div").text,"Price is required")

            #--TRY TO SAVE PRODUCT WITH WRONG DATA
            time.sleep(2)
            driver.find_element(By.ID, 'name').send_keys("test")
            driver.find_element(By.ID, 'description').send_keys("test")
            driver.find_element(By.ID, 'stock').send_keys("test")
            driver.find_element(By.ID, 'price').send_keys("test")

            Select(driver.find_element(By.ID, 'brand_id')).select_by_index(1)
            Select(driver.find_element(By.ID, 'category_id')).select_by_index(1)
            Select(driver.find_element(By.ID, 'product_image_id')).select_by_index(1)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-submit"]'))
            ).click()
            time.sleep(2)

            #--ASSERTS
            proper_text = "SaveBack\nThe price field must be a number. The product image id field must be a number."
            final_alert_xpath = "/html/body/app-root/div/app-products-add-edit/div/form/div[3]/div"
            self.assertEqual(driver.find_element(By.XPATH, final_alert_xpath).text, proper_text)
        finally:
            driver.close()       

    # case 07-001
    def test_display_products_via_brand_filter(self):
        try:
            #--SETUP
            driver = self.set_up_without_login()
            time.sleep(1)
        
            #--SELECT BRAND FILTER
            brand_checkbox = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[data-test^="brand-"]'))
            )
            brand_checkbox.click()

            parent_checkbox_label = brand_checkbox.find_element(By.XPATH, "./..")
            text_from_checkbox = parent_checkbox_label.text

            #--GET DATA FOR ASSERTS
        
            #----filter flag
            time.sleep(1)
            filter_completed_flag = driver.find_element(By.XPATH, '//div[@data-test="filter_completed"]')
        

            #----check if product have proper brand
            selected_product = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-test^="product-"]'))
            )
            selected_product.click()
        
            brand_name = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/p[1]/span[2]'))
            )

            #--ASSERTS
            self.assertTrue(filter_completed_flag is not None)
            self.assertEqual(brand_name.text, text_from_checkbox)
        finally:
            driver.close()

    # case 07-002
    def test_display_product_information(self):
        try:
            #--SETUP
            driver = self.set_up_without_login()
        
            #--SELECT PRODUCT
            selected_product = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-overview/div[3]/div[2]/div[1]/a[1]'))
            )
            selected_product.click()
        
            #--GET DATA FOR ASSERTS
            time.sleep(2)
            product_name = None
            product_price = None
            product_description = None

            product_name = driver.find_element(By.XPATH, '//h1[@data-test="product-name"]')
            product_price = driver.find_element(By.XPATH, '//span[@data-test="unit-price"]')
            product_description = driver.find_element(By.XPATH, '//p[@data-test="product-description"]')
            product_brand = driver.find_element(By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/p[1]/span[2]')
            product_type = driver.find_element(By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/p[1]/span[1]')
        
            #--ASSERTS
            self.assertTrue(product_name is not None)
            self.assertTrue(product_price  is not None)
            self.assertTrue(product_description is not None)
            self.assertTrue(product_brand is not None)
            self.assertTrue(product_type is not None)
        finally:
            driver.close()

    # case 08-001
    def test_display_categories(self):
        driver = webdriver.Chrome()
        driver.get(self.URL)
        time.sleep(2)

        label_1 = driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-overview/div[3]/div[1]/div[2]/label"
        )
        ul_1 = driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-overview/div[3]/div[1]/div[2]/ul"
        )
        label_2 = driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-overview/div[3]/div[1]/div[3]/label"
        )
        ul_2 = driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-overview/div[3]/div[1]/div[3]/ul"
        )
        label_3 = driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-overview/div[3]/div[1]/div[4]/label"
        )
        self.assertEqual(label_1.text, "Hand Tools")
        self.assertTrue(len(ul_1.text) > 0)
        self.assertEqual(label_2.text, "Power Tools")
        self.assertTrue(len(ul_2.text) > 0)
        self.assertEqual(label_3.text, "Other")
        driver.close()  

    # case 09-001
    def test_add_category(self):
        # log in as admin
        driver = self.set_up()

        # go to "categories" page
        self.func.control_panel(driver, "categories")

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
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/div[1]/div/select/option[5]"))
        )
        hammer_option.click()

        # write new category name in "name" field
        driver.find_element(
            By.ID, "name"
        ).send_keys("new hammer category name")

        # write new category slug in "slug" field
        driver.find_element(
            By.ID, "slug"
        ).send_keys("new-hammer-category-name")

        # click "Save" button
        driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/button"
        ).click()

        # wait for save message
        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/div"))
        )

        # check if successful
        self.assertEqual(message.text, "Category saved!")

        # click "back" button
        driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/a"
        ).click()

        time.sleep(3)
        driver.close()  

    # case 09-002
    def test_add_category_with_empty_form(self):
        # log in as admin
        driver = self.set_up()

        # go to "categories" page
        self.func.control_panel(driver, "categories")

        # click "Add category" button
        add_category_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-list/form/div/a"))
        )
        add_category_button.click()

        # click "Save" button
        driver.find_element(
            By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[3]/div/button"
        ).click()

        # wait for save message
        error_message_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/div[2]/div[2]/div"))
        )

        # wait for save message
        error_message_slug = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/div[3]/div[2]/div"))
        )

        self.assertEqual(error_message_name.text, "Name is required")
        self.assertEqual(error_message_slug.text, "Slug is required")
        driver.close()  

    # case 10-001
    def test_delete_category(self):
        #log in as admin
        driver = self.set_up()

        # go to "categories" page
        self.func.control_panel(driver, "categories")

        # find created category by name
        search_bar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/app-root/div/app-list/form/div/input"))
        )
        # search_bar.send_keys("new hammer category name")
        search_bar.send_keys("new hammer category name")

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

        # get toast message
        delete_toast_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "body > app-root > app-toasts > ngb-toast"))
        ).text

        # check if category deletion was successful
        self.assertEqual(delete_toast_message, "Category deleted.")
        driver.close()  


if __name__ == "__main__":
     unittest.main()
