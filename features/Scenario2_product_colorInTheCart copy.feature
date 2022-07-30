Feature: Scenario2_product_colorInTheCart

    Scenario: Selecting a Color based on DB and adding the product to the cart
        when we are alredy on the page of the offer
        And collects more details from the product 
        And Get color and more details from Database based on the notebooks name
        And select the color and add to the cart
        Then The product is on the right color inside of the cart
#Then the product is on the cart with the right color
        