Feature: Adding a brand
    As a user
    I want to add a brand
    So that it appears in the brands table

    Scenario: Add a brand and verify its presence in the table
        Given the user is on the Brands page
        When the user adds a brand with Slug "testing" and Name "testing"
        Then the brand with Slug "testing" and Name "testing" should appear in the brands table
