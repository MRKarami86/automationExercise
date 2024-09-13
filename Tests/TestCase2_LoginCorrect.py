import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://automationexercise.com")
        self.driver.maximize_window()
        self.LoginPage = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_Successful(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "//a[contains(.,'Signup / Login')]").click()
        try:
            signupForm = self.driver.find_element(By.XPATH, "//div[@class='login-form']//h2[1]")
            signupFormTest = signupForm.text
            assert signupFormTest == "Login to your account"
            print("Verify 'Login to your account' is visible")
        except AssertionError:
            print("AssertionError: expected 'Login to your account'")

        self.LoginPage.login("mrkarami86@gmail.com", "12345678")

        try:
            loginUser = self.driver.find_element(By.XPATH, "//i[@class='fa fa-user']/following-sibling::b[1]")
            loginUserText = loginUser.text
            userName = "MRKarami"
            assert loginUserText == userName
            print(f"Verify that 'Logged in as {userName}' is visible")
        except AssertionError:
            print(f"AssertionError: expected 'Logged in as {userName}'")


        #First SignUpPage
        self.SignUpPage.Delete_Account()
        try:
            accountDeleted = self.driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
            accountDeletedText = accountDeleted.text
            assert accountDeletedText == "ACCOUNT DELETED!"
            print("Verify that 'ACCOUNT DELETED!' is visible")
        except AssertionError:
            print("AssertionError: expected 'ACCOUNT DELETED!'")

        self.driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()


if __name__ == "__main__":
    unittest.TestCase()
