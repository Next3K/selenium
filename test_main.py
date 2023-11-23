import time
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
    # def test_update_product(self):
    #
    #     #--SETUP
    #     driver = self.set_up()
    #
    #     #--LOGIN
    #     func.login_method(driver)
    #
    #     #--GO TO PRODUCT PANEL
    #     func.control_panel(driver, "products")
    #
    #     #--SELECT PRODUCT
    #     rows = driver.find_elements(By.XPATH, '//tbody/tr')
    #     target_id = "01HFW6ET98CZ3YS40S05SZKC7Q"
    #     row_with_product = func.find_element_from_table(driver, target_id)
    #
    #     edit_button = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, './/a[@data-test="product-edit-' + target_id + '"]'))
    #     )
    #     edit_button.click()
    #
    #     #--EDIT PRODUCT DETAILS
    #     price_input = WebDriverWait(driver, 3).until(
    #         EC.visibility_of_element_located((By.ID, 'price'))
    #     )
    #     price_input.clear()
    #     price_input.send_keys(5)
    #
    #     #--SAVE PRODUCT DETAILS
    #     btn_save = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//button[@data-test="product-submit"]'))
    #     )
    #     btn_save.click()
    #     edit_completed_flag = driver.find_element(By.XPATH, '//div[@role="alert"]')
    #
    #     btn_back = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//a[@data-test="back"]'))
    #     )
    #     btn_back.click()
    #
    #     #--ASSERTS
    #     row_with_edited_product = func.find_element_from_table(driver, target_id)
    #
    #     actual_price = row_with_edited_product.find_element(By.XPATH, './/td[4]').text
    #     expected_price = "$5.00"
    #
    #     assert actual_price == expected_price, "not edited"
    #
    #
    #     self.fail()

    # case 06-001
    # def test_remove_product(self):
    #     #--SETUP
    #     driver = self.set_up()
    #
    #     #--LOGIN
    #     func.login_method(driver)
    #
    #     #--GO TO PRODUCT PANEL
    #     func.control_panel(driver, "products")
    #
    #     #--SELECT PRODUCT
    #     rows = driver.find_elements(By.XPATH, '//tbody/tr')
    #     target_id = "01HFW6ET98CZ3YS40S05SZKC7Q"
    #     row_with_product = func.find_element_from_table(driver, target_id)
    #
    #     #--DELETE PRODUCT
    #     delete_button = row_with_product.find_element(By.XPATH, './/a[@data-test="product-delete-' + target_id + '"]')
    #     delete_button.click()
    #
    #     product_deleted_flag = WebDriverWait(driver, 2).until(
    #         EC.presence_of_element_located((By.XPATH, '//div[@class="toast-body" and contains(text(), "Product deleted.")]'))
    #     )
    #
    #     #--ASSERTS
    #     row_with_product = func.find_element_from_table(driver, target_id)
    #     assert row_with_product is None, "Product not removed"

    # case 07-001
    # def test_display_products_via_brand_filter(self):
    #     #--SETUP
    #     driver = self.set_up()
    #
    #     time.sleep(1)
    #     brand = "01HFW9WNQTZ1Y53XWRC6X63AG5"
    #
    #     #--SELECT BRAND FILTER
    #
    #     checkbox = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//input[@data-test="brand-'+brand+'"]'))
    #     )
    #     checkbox.click()
    #
    #     #--ASSERTS
    #
    #     #----filter flag
    #     filter_completed_flag = WebDriverWait(driver, 3).until(
    #         EC.presence_of_element_located((By.XPATH, '//input[@data-test="filter_completed"]'))
    #     )
    #     assert filter_completed_flag not None, "Not filtered"
    #
    #     #----check if product have proper brand
    #     selected_product = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//a[@data-test="product-01HFW9WNRBXR513FE6RP0FJYW8"]'))
    #     )
    #     selected_product.click()
    #
    #     brand_name = WebDriverWait(driver, 3).until(
    #         EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-detail/div[1]/div[2]/p[1]/span[2]'))
    #     )
    #     assert brand_name.text == "Brand name 1", "Wrong brand"

    # case 07-002
    # def test_display_product_information(self):
    #     #--SETUP
    #     driver = self.set_up()
    #
    #     #--SELECT PRODUCT
    #     selected_product = WebDriverWait(driver, 5).until(
    #         EC.element_to_be_clickable((By.XPATH, '//a[@data-test="product-01HFW9WNRBXR513FE6RP0FJYW8"]'))
    #     )
    #     selected_product.click()
    #
    #     #--ASSERTS
    #     time.sleep(3)
    #     product_name = driver.find_element(By.XPATH, '//a[@data-test="product-name"]')
    #     product_price = driver.find_element(By.XPATH, '//a[@data-test="unit-price"]')
    #     product_description = driver.find_element(By.XPATH, '//a[@data-test="product-description"]')
    #
    #     assert "" == product_name, "Names are not the same"
    #     assert "" == product_price, "Price are not the same"
    #     assert "" == product_description, "Description are not the same"

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
                                              "/html/body/app-root/div/app-categories-add-edit/div/form/div[2]/div/"
                                              "div[1]/div/select/option[5]"))
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

    # case 10-001
    def test_delete_category(self):
        # log in as admin
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
