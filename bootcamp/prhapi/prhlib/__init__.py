import requests
import json

def get_company_info(id):
    """
    This is a simple function that allows you to pull data from PRH API

    >>> get_company_info('0912797-2')
    'Noksu Oy'
    """
    url = f"https://avoindata.prh.fi/tr/v1/{id}"

    payload = ""
    response = requests.request("GET", url, data=payload)
    if response.status_code == 200:
        company = json.loads(response.text)
        return company['results'][0]['name']
    else:
        return False