# Created by rima at 4/28/2022
Feature: Tests for cart page and cart icon


  Scenario: User can click on the cart icon ,it opens Empty Cart page if no products were added.
    Given Open Get top
    When Click on the cart icon.
    Then Verify empty cart page.

  Scenario: User can see the popup message,When hover over the mouse to the cart icon.
    Given Open Get top
    When Hover the mouse to cart icon.
    Then Verify a popup message"No products in the cart."

