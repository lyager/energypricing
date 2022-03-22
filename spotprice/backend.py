import sqlite3


class Backend:

    def __init__(self):
        self.con = sqlite3.connect('spotprice.sql')
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute('''CREATE TABLE spotprice
                                (id, HourUTC, HourDK, PriceArea,
                                 SpotPriceDKK, SpotPriceEur)''')
            self.con.commit()
        except sqlite3.OperationalError:
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
