Feature: Search Products

  Scenario: User searches for a product
    Given the browser is launched
    When I navigate to the url "https://automationexercise.com"
    Then the home page should be visible
    When I click on the "Products" button
    Then I should be navigated to the "ALL PRODUCTS" page
    When I enter "Winter Top" in the search input and click search button
    Then "SEARCHED PRODUCTS" should be visible
    And all the products related to search should be visible
