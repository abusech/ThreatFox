#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 2:
    print("Usage: python3 threatfox_query_recent-iocs.py <number-of-days>")
    quit()

pool = urllib3.HTTPSConnectionPool('threatfox-api.abuse.ch', port=443, maxsize=50)

data = {
    'query':    'get_iocs',
    'days':     sys.argv[1]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
