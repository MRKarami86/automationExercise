from Locators.Locators import Locators
from selenium.webdriver.support.ui import Select


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://automationexercise.com")
        self.Locators = Locators()

    def SignUp(self, SignUpName, SignUpEmail):
        self.driver.find_element(*self.Locators.SignUpName).send_keys(SignUpName)
        self.driver.find_element(*self.Locators.SignUpEmail).send_keys(SignUpEmail)
        self.driver.find_element(*self.Locators.SignUpButton).click()

    def SignUpInformation(self, SignUpPassword, Day_Value, Months_value, Years_value):
        self.driver.find_element(*self.Locators.RadioButton_Mr).click()
        self.driver.find_element(*self.Locators.SignUpPassword).send_keys(SignUpPassword)
        select_list_days = self.driver.find_element(*self.Locators.ListDays_select)
        select_days = Select(select_list_days)
        select_days.select_by_value(Day_Value)
        select_list_months = self.driver.find_element(*self.Locators.ListMonths_select)
        select_months = Select(select_list_months)
        select_months.select_by_value(Months_value)
        select_list_years = self.driver.find_element(*self.Locators.ListYears_select)
        select_years = Select(select_list_years)
        select_years.select_by_value(Years_value)
        self.driver.find_element(*self.Locators.Newsletter_checkbox).click()
        self.driver.find_element(*self.Locators.OptIn_checkbox).click()
        print(self.driver.current_url)

    def address_information(self, FirstName, LastName, Company, Address, Address2, Country_Value, State, City,
                            Zipcode, MobileNumber):
        self.driver.find_element(*self.Locators.First_Name).send_keys(FirstName)
        self.driver.find_element(*self.Locators.Last_Name).send_keys(LastName)
        self.driver.find_element(*self.Locators.Company).send_keys(Company)
        self.driver.find_element(*self.Locators.Address).send_keys(Address)
        self.driver.find_element(*self.Locators.Address2).send_keys(Address2)
        select_country = self.driver.find_element(*self.Locators.Country_Select)
        select_country_value = Select(select_country)
        select_country_value.select_by_value(Country_Value)
        self.driver.find_element(*self.Locators.State).send_keys(State)
        self.driver.find_element(*self.Locators.City).send_keys(City)
        self.driver.find_element(*self.Locators.Zipcode).send_keys(Zipcode)
        self.driver.find_element(*self.Locators.MobileNumber).send_keys(MobileNumber)
        self.driver.find_element(*self.Locators.Create_Account_Button).click()

    def Delete_Account(self):
        self.driver.find_element(*self.Locators.Delete_Account_Button).click()

