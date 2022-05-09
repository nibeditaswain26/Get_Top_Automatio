# Created by rima at 4/26/2022
Feature: Tests for product page


  Scenario: User can see left arrow clickable button and right arrow clickable on right side of the page.
    Given Open Get top
    When Hover over the mouse to IPAD.
    And Hover the mouse to ipad mini button and click on it.
    Then User can see a left clickable button and right clickable button.

  Scenario: User can see product's "user ratting" on the product details page.
    Given Open Get top
    When Hover over the mouse to IPAD.
    And Hover the mouse to ipad button and click on it.
    Then Verify user can see the product's user ratting between product name and price of the product.

  Scenario: Add product to the cart and verify the price.
    Given Open Get top
    When Hover over the mouse to MAC.
    And Hover the mouse to MacBook Pro 13-inch button and click on it.
    And Click on ADD TO CART button.
    Then Verify that price in top nav menu is correct.
    Then verify that amount of items shown in top nav menu are correct


  Scenario: Add products to cart,hover over cart icon,verify correct products.
   Given Open Get top
    When Hover over the mouse to MAC.
    And Hover the mouse to MacBook Pro 13-inch button and click on it.
    And Click on ADD TO CART button.
    And Hover the mouse to cart icon.
    Then verify correct products and subtotal shown
    Then Verify user can click on "View Cart" and is taken to cart page



  Scenario: Add products to cart,hover over cart icon,verify subtotal shown
   Given Open Get top
    When Hover over the mouse to MAC.
    And Hover the mouse to MacBook Pro 13-inch button and click on it.
    And Click on ADD TO CART button.
    And Hover the mouse to cart icon.
    Then Verify user can click on "Checkout" and is taken to checkout page

  Scenario: Add a product to cart, hover over cart icon, verify user can remove a product
   Given Open Get top
    When Hover over the mouse to MAC.
    And Hover the mouse to MacBook Pro 13-inch button and click on it.
    And Click on ADD TO CART button.
    And Hover the mouse to cart icon.
    Then Verify user can remove a product.
