import sqlite3
import logging


class Backend:

    def __init__(self, logging: logging):
        self.inserted = 0
        self.duplicates = 0
        self.logging = logging
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
            self.logging.warning("Database {} already exists, will not create tables".format(db_name))
            pass

    def __del__(self):
        self.con.close()
        self.logging.info("Inserted: {} dupclicates: {}".format(self.inserted, self.duplicates))

    def add_price(self, id, hourutc, hourdk, pricearea, spotpricedkk, spotpriceeur):
        """
            "_id": 2029995,
            "HourUTC": "2022-03-22T22:00:00+00:00",
            "HourDK": "2022-03-22T23:00:00",
            "PriceArea": "DK2",
            "SpotPriceDKK": 1654.68,
            "SpotPriceEUR": 222.38
        """
        try:
            self.cursor.execute("INSERT INTO spotprice VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(id, hourutc, hourdk, pricearea, spotpricedkk, spotpriceeur))
            self.con.commit()
            self.inserted += 1
        except sqlite3.IntegrityError:
            # Unique id's are counted and ignored
            self.duplicates += 1
            pass
