#!/bin/sh

http --output ./spotprice-$(date +\%Y\%m\%d\%H\%M\%S).json GET 'https://api.energidataservice.dk/datastore_search?resource_id=elspotprices&sort=HourDK desc'

