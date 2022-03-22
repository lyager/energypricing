import sqlite3
import logging


class Backend:

    def __init__(self, logging: logging):
        db_name = "spotprice.sql"
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute('''CREATE TABLE spotprice
                                (id INTEGER NOT NULL PRIMARY KEY,
                                HourUTC,
                                HourDK,
                                PriceArea,
                                SpotPriceDKK,
                                SpotPriceEur)''')
            self.con.commit()
        except sqlite3.OperationalError:
            logging.warning("Database {} already exists, will not create tables".format(db_name))
            pass

    def add_price(self, id, hourutc, hourdk, pricearea, spotpricedkk, spotpriceeur):
        """
            "_id": 2029995,
            "HourUTC": "2022-03-22T22:00:00+00:00",
            "HourDK": "2022-03-22T23:00:00",
            "PriceArea": "DK2",
            "SpotPriceDKK": 1654.68,
            "SpotPriceEUR": 222.38
        """
        self.cursor.execute("INSERT INTO spotprice VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(id, hourutc, hourdk, pricearea, spotpricedkk, spotpriceeur))
        self.con.commit()
