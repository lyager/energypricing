# Energy Pricing

## About

Plotting a 24-hour forecast of electricity pricing.

## Goals

- Make a Telegram channel to push new pricing updates
- Put historic results into a database
- Docker as deployment

## Development notes

Getting the latest prices

  http 'https://api.energidataservice.dk/datastore_search?resource_id=elspotprices&filters={"PriceArea":"DK2"}'



