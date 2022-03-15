#!/usr/bin/env python3
# Rough POC

import pandas
import chartify
import json

with open('tests/data/example.json') as fp:
    j = json.load(fp)

j_records = j['result']['records']

p = pandas.DataFrame(j_records)
c = chartify.Chart(x_axis_type='datetime', y_axis_type='linear')
c.set_title("Latest Electricity Prices")
c.set_subtitle("Latest Elecitricy prices for DK2")
c.axes.set_xaxis_label("Date")
c.axes.set_yaxis_label("Price in DKK")
c.plot.line(p, 'HourDK', 'SpotPriceDKK')
c.show('html')
