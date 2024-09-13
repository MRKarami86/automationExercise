from typing import Tuple

from selenium.webdriver.common.by import By


class Locators:
    # صفحه ثبت نام
    SignUpName = (By.XPATH, "//input[@data-qa='signup-name']")
    SignUpEmail = (By.XPATH, "//input[@data-qa='signup-email']")
    SignUpButton = (By.XPATH, "//button[@data-qa='signup-button']")
    # ENTER ACCOUNT INFORMATION
    RadioButton_Mrs = (By.XPATH, "//input[@value='Mrs']")
    RadioButton_Mr = (By.XPATH, "//input[@value='Mr']")
    SignUpPassword = (By.XPATH, "//input[@data-qa='password']")
    ListDays_select = (By.XPATH, "//select[@data-qa='days']")
    ListMonths_select = (By.XPATH, "//select[@data-qa='months']")
    ListYears_select = (By.XPATH, "//select[@data-qa='years']")
    Newsletter_checkbox = (By.ID, "newsletter")
    OptIn_checkbox = (By.ID, "optin")
    # ADDRESS INFORMATION
    First_Name = (By.XPATH, "//input[@data-qa='first_name']")
    Last_Name = (By.XPATH, "//input[@data-qa='last_name']")
    Company = (By.XPATH, "//input[@data-qa='company']")
    Address = (By.XPATH, "//input[@data-qa='address']")
    Address2 = (By.XPATH, "//input[@data-qa='address2']")
    Country_Select =(By.XPATH, "//select[@data-qa='country']")
    City = (By.XPATH, "//input[@data-qa='city']")
    State = (By.XPATH, "//input[@data-qa='state']")
    Zipcode = (By.XPATH, "//input[@data-qa='zipcode']")
    MobileNumber = (By.XPATH, "//input[@data-qa='mobile_number']")
    Create_Account_Button = (By.XPATH, "(//button[@type='submit'])[1]")
    # ACCOUNT CREATED!
    Account_text = (By.XPATH, "//b[text()='Account Created!']")
    Continue_Button = (By.XPATH, "//a[@data-qa='continue-button']")
    # Delete ACCOUNT
    Delete_Account_Button = (By.XPATH, "//a[contains(.,'Delete Account')]")
    Account_text_Delete = (By.XPATH, "//b[text()='Account Deleted!']")
    Continue_Account_Button_Delete = (By.XPATH, "//a[@data-qa='continue-button']")
    # صفحه لاگین
    Email = (By.XPATH, "//input[@data-qa='login-email']")
    Password = (By.XPATH, "//input[@data-qa='login-password']")
    Login_Button = (By.XPATH, "//button[@data-qa='login-button']")
    #صفحه ارتباط با ما
    nameContactUs = (By.XPATH, "//input[@data-qa='name']")
    emailContactUs = (By.XPATH, "//input[@data-qa='email']")
    subjectContactUs = (By.XPATH, "//input[@data-qa='subject']")
    messageContactUs = (By.XPATH, "//textarea[@data-qa='message']")
    fileUploadButton = (By.XPATH, "//input[@type='file']")
    submitButton = (By.XPATH, "//input[@data-qa='submit-button']")
    # صفحه محصولات
    searchInput = (By.ID, "search_product")
    searchButton = (By.ID, "submit_search")
