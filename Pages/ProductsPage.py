from Locators.Locators import Locators


class ProductsPage():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def searchBox(self, productName):
        self.driver.find_element(*self.locator.searchInput).send_keys(productName)
        self.driver.find_element(*self.locator.searchButton).click()
