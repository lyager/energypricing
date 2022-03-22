import requests


def main():
    payload = {
        'resource_id': 'elspotprices',
        'sort': 'HourDK desc'
    }
    r = requests.get("https://api.energidataservice.dk/datastore_search",
                     params=payload)
    r.raise_for_status()
    j = r.json()
    print(j)


if __name__ == "__main__":
    main()
