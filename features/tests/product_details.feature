# Created by rima at 4/26/2022
Feature: Tests for product page


  Scenario: User can see left arrow clickable button and right arrow clickable on right side of the page.
    Given Open Get top
    When Hover over the mouse to <IPAD>.
    And Hover the mouse to <ipad mini> button and click on it.
    Then User can see a left clickable button and right clickable button.