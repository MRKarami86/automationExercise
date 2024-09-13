from Locators.Locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.Locators = Locators()

    def login(self, email, password):
        self.driver.find_element(*self.Locators.Email).send_keys(email)
        self.driver.find_element(*self.Locators.Password).send_keys(password)
        self.driver.find_element(*self.Locators.Login_Button).click()