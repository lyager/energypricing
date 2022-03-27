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
        backend.add_price(i['_id'], i['HourUTC'], i['HourDK'],
                          i['PriceArea'], i['SpotPriceDKK'], i['SpotPriceEUR'])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch latest Energy prices")
    parser.add_argument("--logging", help="Logging location", action="store",
                        type=str)
    args = parser.parse_args()

    if args.logging:
        # Setup logging to file
        logging.basicConfig(filename="{}/spotprice.log".format(args.logging),
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
    else:
        logging.getLogger().setLevel(logging.INFO)

    j = get_json()
    b = Backend(logging)
    to_backend(j, b)
    del b
