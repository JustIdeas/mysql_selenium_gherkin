Feature: Scenario4_product_removeProductCart

    Scenario: Validating checkout page
        when Openning the browser
        And Access offer and takes all information
        And Add "1" products and add to the cart
        And going to checkout
        Then the cart should show "Your shopping cart is empty"     