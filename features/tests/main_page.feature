# Created by rima at 5/2/2022
Feature: Tests for main page


  Scenario: User can Operate the product banners.
    Given Open Get top
    When User can click right and left arrows to see top banners.
    When User can click bottom dots to see top banner.
    When User can click on product banner,Then verify it is taken to correct category page.
