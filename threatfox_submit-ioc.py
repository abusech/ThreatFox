#!/usr/bin/python3
import requests
import urllib3
import json

# Prepare HTTPSConnectionPool
headers = {
  "API-KEY":        "YOUR-API-KEY-HERE",
}
pool = urllib3.HTTPSConnectionPool('threatfox-api.abuse.ch', port=443, maxsize=50, headers=headers, cert_reqs='CERT_NONE', assert_hostname=True)

# threat_type      - Query https://threatfox.abuse.ch/api/#types to get the appropriate
#                    threat_type / ioc_type combination
# ioc_type         - Query https://threatfox.abuse.ch/api/#types to get the appropriate
#                    threat_type / ioc_type combination
# malwareinfo      - Query https://threatfox.abuse.ch/api/#malware-list to get the appropriate
#                  - malware family or search through Malpedia web UI: https://malpedia.caad.fkie.fraunhofer.de/
# confidence_level - Optional; Must be between 0-100. Default: 50
# reference        - Optional; Must be a URL if provided
# Comment          - Optional; Your comment on the IOC(s) you want to submit
# anonymous        - Optional; 0 (false) or 1 (true). Default: 0 (false)
# tag_list         - Optional; List of tags
# iocs             - list of IOCs you want to submit

data = {
    'query':            'submit_ioc',
    'threat_type':      threat_type,
    'ioc_type':         ioc_type,
    'malware':          malware,
    'confidence_level': confidence_level,
    'reference':        reference,
    'comment':          comment,
    'anonymous':        0,
    'tags': [
        tag
    ],
    'iocs': [
        ioc
    ]
}
json_data = json.dumps(data)
response = pool.request("POST", "/api/v1/", body=json_data)
response = response.data.decode("utf-8", "ignore")
print(response)
