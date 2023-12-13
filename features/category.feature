# Created by Julek at 12.12.2023
Feature: Category management
  As an admin
  I want to add a category
  So that I can see the "category saved" message
  Next I want to delete that category
  So that I can see the delete message

  Scenario: Create and delete category
    Given the user is logged in as an admin
    And the user is on the Categories page
    When the user adds a new category with name "new hammer category name" and slug "new-hammer-category-name"
    Then the user should see a category add success message "Category saved!"
    And the user deletes the category with name "new hammer category name"
    Then the user should see a category delete success message "Category deleted."