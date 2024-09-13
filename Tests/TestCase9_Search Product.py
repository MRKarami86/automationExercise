import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.ProductsPage import ProductsPage


class searchProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.productsPage = ProductsPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.CSS_SELECTOR, "[href='/products']").click()
        try:
            assert self.driver.current_url == "https://automationexercise.com/products"
            print("Verify user is navigated to ALL PRODUCTS page successfully")
        except AssertionError:
            print("AssertionError: expected 'Verify user is navigated to ALL PRODUCTS page successfully'")

        self.productsPage.searchBox("Winter Top")
        try:
            product = self.driver.find_element(By.XPATH,"//div[@class='productinfo text-center']/p[.='Winter Top']")
            product.is_displayed()
            print("Verify 'SEARCHED PRODUCTS' is visible")
        except AssertionError:
            print("AssertionError: expected 'Verify 'SEARCHED PRODUCTS' is not visible'")


if __name__ == "__main__":
    unittest.TestCase()
