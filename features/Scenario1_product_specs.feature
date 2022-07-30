Feature: Scenario1_product_specs

    Scenario: Validating all informations of the notebook on the website from the Database
        When Openning the browser
        When Access offer and takes all information
        And Get information from Database bases on the notebooks name
        then all info from website and database should be the same