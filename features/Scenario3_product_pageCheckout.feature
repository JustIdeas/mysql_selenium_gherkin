Feature: Scenario3_product_pageCheckout

    Scenario: Validating checkout page
        when on the main page
        And look from the "HP PAVILION 15Z TOUCH LAPTOP" on the search box
        And changing the color to "YELLOW"
        And Add "4" products and add to the cart
        And Access the checkout and validate the sum of the product and compare to the sum of the website
        Then update the database with the color used on the product "HP PAVILION 15Z TOUCH LAPTOP" in the website
        