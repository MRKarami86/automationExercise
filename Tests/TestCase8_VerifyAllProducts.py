import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "(//ul[@class='nav navbar-nav']//a)[2]").click()
        try:
            productPage = self.driver.find_element(By.XPATH, "(//div[@class='features_items']//h2)[1]")
            productPageTest = productPage.text
            assert productPageTest == "ALL PRODUCTS"
            print("Verify user is navigated to ALL PRODUCTS page successfully")
        except AssertionError:
            print("AssertionError: expected 'Verify user is navigated to ALL PRODUCTS page successfully'")

        self.driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()


if __name__ == "__main__":
    unittest.TestCase()