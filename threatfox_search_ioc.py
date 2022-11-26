#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python3 threatfox_search_ioc.py <search-term>")
    quit()

pool = urllib3.HTTPSConnectionPool('threatfox-api.abuse.ch', port=443, maxsize=50)

data = {
    'query':            'search_ioc',
    'search_term':      sys.argv[1]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
