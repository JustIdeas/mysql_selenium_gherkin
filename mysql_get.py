from dataclasses import dataclass
import mysql.connector
import setup




class db_notebooks():

    def __init__(self, parameter = '') -> None:
        self.mydb = mysql.connector.connect(
            host=setup.mysql_ip,
            user=setup.db_login,
            password=setup.db_password,
            database=setup.db_name
        )
        self.parameter = parameter
        self.cursor = self.mydb.cursor()
        self.result = self.fetch_values()
        self.product_info = {
            "ID": self.result[0],
            "PRODUCT_NAME": self.result[1].replace("\n", " "),
            "CUSTOMIZATION": self.result[2].replace("\n", " "),
            "DISPLAY": self.result[3].replace("\n", " "),
            "DISPLAY_RESOLUTION": self.result[4].replace("\n", " "),
            "DISPLAY_SIZE": self.result[5].replace("\n", " "),
            "MEMORY": self.result[6].replace("\n", " "),
            "OPERATING_SYSTEM": self.result[7].replace("\n", " "),
            "PROCESSOR": self.result[8].replace("\n", " "),
            "TOUCHSCREEN": self.result[9].replace("\n", " "),
            "WEIGHT":self.result[10].replace("\n", " "),
            "COLOR": self.result[11].replace("\n", " ")
        }



    def fetch_values(self):
        self.cursor.execute("SELECT * FROM massas;")
        result = self.cursor.fetchall()
        for index in result:
            if self.parameter in index[1::][0]:
                return index
            else:
                raise ValueError("Não achou o monitor na base")
    def get_productname(self):
        return self.product_info["PRODUCT_NAME"]
    def get_customization(self):
        return self.product_info["CUSTOMIZATION"]
    def get_display(self):
        return self.product_info["DISPLAY"]
    def get_displayresolution(self):
        return self.product_info["DISPLAY_RESOLUTION"]
    def get_displaysize(self):
        return self.product_info["DISPLAY_SIZE"]
    def get_memory(self):
        return self.product_info["MEMORY"]
    def get_operatingsystem(self):
        return self.product_info["OPERATING_SYSTEM"]
    def get_processor(self):
        return self.product_info["PROCESSOR"]
    def get_touchscreen(self):
        return self.product_info["TOUCHSCREEN"]
    def get_weight(self):
        return self.product_info["WEIGHT"]
    def get_color(self):
        return self.product_info["COLOR"]
    def get_all(self):
        return self.product_info
    def get_id(self):
        return self.product_info["ID"]
    def update_values(self, ID, Column, Value):
        self.cursor.execute(f"UPDATE massas SET {Column} = '{Value}' WHERE IDMASSAS = {ID};")
        self.mydb.commit()
