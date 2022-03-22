import requests
import logging
from backend import Backend


def get_json():
    payload = {
        'resource_id': 'elspotprices',
        'sort': 'HourDK desc'
    }
    r = requests.get("https://api.energidataservice.dk/datastore_search",
                     params=payload)
    r.raise_for_status()
    j = r.json()
    assert j['success']
    return j


def to_backend(json, backend: Backend):
    for i in json['result']['records']:
        backend.add_price(i['_id'], i['HourUTC'], i['HourDK'], i['PriceArea'], i['SpotPriceDKK'], i['SpotPriceEUR'])


if __name__ == "__main__":
    j = get_json()
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    b = Backend(logging)
    to_backend(j, b)
