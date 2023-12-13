Feature: Update a product details
    As an admin
    I want to update the details of a product
    So that the changes are reflected in both the product list and page of the product 

    Scenario: Update product details and verify the changes
        Given the user is logged as an admin
        And the user is on the Products panel in the administrator's dashboard
        When the user selects a product to edit
        And edits the product details
        And the user goes back to the product list
        And the user searches for the edited product
        Then the updated product with the new data should appear in the product list
        And the browser is closed