#!/usr/bin/python3
import requests
import urllib3
import json
import sys

if len(sys.argv) < 3:
    print("Script to query ThreatFox for Indicators Of Compromise (IOCs) associated with a specific tag")
    print("Usage: python3 threatfox_query_tag.py <tag>")
    print("Note: If you don't have an Auth-Key yet, you can obtain one at https://auth.abuse.ch/")
    quit()

headers = {
    "Auth-Key"      :   sys.argv[1]
}

pool = urllib3.HTTPSConnectionPool('threatfox-api.abuse.ch', port=443, maxsize=50, headers=headers)

data = {
    'query':            'taginfo',
    'tag':              sys.argv[2]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
