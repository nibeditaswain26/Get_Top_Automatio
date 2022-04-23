# Created by rima at 4/22/2022
Feature: Test  for "iPhone 12" button in IPHONE dropdown .
  # Enter feature description here

  Scenario: User can  go to the selected page after click on the "iphone 12" button.
    Given Open Get top
    When Hover over the mouse to “IPHONE”.
    And Hover the mouse to "iphone 12" button and click on it.
    Then Verify user goes to the page of the iphone 12.
