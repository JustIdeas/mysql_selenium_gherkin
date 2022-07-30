The Idea of this project is to mainly test the interaction with an specific notebook, cart, checkout and Database. 

These interactions are separated by 4 scenarios:
    1° - Make sure that the notebook offer has the same specs as the database have from the same notebook;
    2° - Change the color of the notebook and compare with the database color of the same notebook;
    3° - Make sure that the checkout is calculating all the sum of more than 1 notebook at the total field;
    4° - Remove the product of the cart and make sure that is empty.

To run these you will need to have:
    * MYSQL Database;
    * Python3, selenium webdriver (firefox) and behave (for gherkin);
 
To run the project:
    Run {behave} command inside of this project, after the installations of the dependences mentioned before.

Mysql Database structure:

CREATE DATABASE `banco_teste_automacao`; CREATE TABLE `massas` ( `IDMASSAS` int(11) NOT NULL AUTO_INCREMENT, `NAME_PRODUCT` varchar(45) DEFAULT NULL, `CUSTOMIZATION` varchar(45) DEFAULT NULL, `DISPLAY` varchar(600) DEFAULT NULL, `DISPLAY_RESOLUTION` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL, `DISPLAY_SIZE` varchar(45) DEFAULT NULL, `MEMORY` varchar(45) DEFAULT NULL, `OPERATING_SYSTEM` varchar(45) DEFAULT NULL, `PROCESSOR` varchar(255) DEFAULT NULL, `TOUCHSCREEN` varchar(45) DEFAULT NULL, `WEIGHT` varchar(45) DEFAULT NULL, `COLOR` varchar(45) DEFAULT NULL, PRIMARY KEY (`IDMASSAS`) ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; 

insert into massas(NAME_PRODUCT,CUSTOMIZATION,DISPLAY,DISPLAY_RESOLUTION,DISPLAY_SIZE,MEMORY,OPERATING_SYSTEM,PROCESSOR,TOUCHSCREEN,WEIGHT,COLOR) values("HP PAVILION 15Z TOUCH LAPTOP","Simplicity","15.6-inch diagonal Full HD WLED-backlit Display (1920x1080) Touchscreen","1920x1080","15.6","16GB DDR3 - 2 DIMM","Windows 10","AMD Quad-Core A10-8700P Processor + AMD Radeon(TM) R6 Graphics","Yes","5.51 lb","GRAY");
