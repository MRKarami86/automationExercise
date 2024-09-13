import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Pages.SignUpPage import SignUpPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.SignUpPage = SignUpPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_signup(self):
        try:
            assert self.driver.current_url == "https://automationexercise.com/"
            print("Verify that home page is visible successfully")
        except AssertionError:
            print("AssertionError: expected 'https://automationexercise.com/'")

        self.driver.find_element(By.XPATH, "//a[contains(.,'Signup / Login')]").click()
        try:
            signupForm = self.driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
            signupFormTest = signupForm.text
            assert signupFormTest == "New User Signup!"
            print("Verify 'New User Signup!' is visible")
        except AssertionError:
            print("AssertionError: expected 'New User Signup!'")

        self.SignUpPage.SignUp("MRKarami86", "mrkarami86@gmail.com")
        try:
            Account = self.driver.find_element(By.XPATH, "//b[text()='Enter Account Information']")
            accountText = Account.text
            assert accountText == "ENTER ACCOUNT INFORMATION"
            print("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
        except AssertionError :
            print("AssertionError: expected 'ENTER ACCOUNT INFORMATION'")

        self.SignUpPage.SignUpInformation('12345678', '5', '5', '1989')
        self.SignUpPage.address_information('MRK', 'Karami', 'TestCompany'
                                            , 'tehranCity', 'Tehran', 'India'
                                            , 'Teh', 'Tehran', '021', '09192438902')
        try:
            accountCreated = self.driver.find_element(By.XPATH, "//b[text()='Account Created!']")
            accountCreatedText = accountCreated.text
            assert accountCreatedText == "ACCOUNT CREATED!"
            print("Verify that 'ACCOUNT CREATED!' is visible")
        except AssertionError:
            print("AssertionError: expected 'ACCOUNT CREATED!'")

        self.driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()
        WebDriverWait(self.driver, 2)
        try:
            loginUser = self.driver.find_element(By.XPATH, "//i[@class='fa fa-user']/following-sibling::b[1]")
            loginUserText = loginUser.text
            userName = "MRKarami86"
            assert loginUserText == userName
            print(f"Verify that 'Logged in as {userName}' is visible")
        except AssertionError:
            print(f"AssertionError: expected 'Logged in as {userName}'")

        self.SignUpPage.Delete_Account()
        try:
            accountDeleted = self.driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
            accountDeletedText = accountDeleted.text
            assert accountDeletedText == "ACCOUNT DELETED!"
            print("Verify that 'ACCOUNT DELETED!' is visible")
        except AssertionError:
            print("AssertionError: expected 'ACCOUNT DELETED!'")

        self.driver.find_element(By.XPATH, "//a[@data-qa='continue-button']").click()


if __name__ == '__main__':
    unittest.main()
