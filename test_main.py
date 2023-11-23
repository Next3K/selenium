from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functions import Functions


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
        driver = self.set_up()

    # case 02-001
    def test_add_brand(self):
        driver = self.set_up()

    # case 03-001
    def test_delete_brand(self):
        driver = self.set_up()

    # case 04-001
    def test_update_brand(self):
        driver = self.set_up()

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
