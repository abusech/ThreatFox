# ThreatFox
ThreatFox is an open threat intelligence sharing platform, allowin anyone to share indicators of compromise (IOCs). This repository provides some sample python3 scripts on how to interact with the ThreatFox API.

## Query recent IOCs
This script calls ThreatFox's [recent IOC endpoint](https://threatfox.abuse.ch/api/#recent-iocs) which returns the most recent IOCs added to ThreatFox. The example below queries the endpoint for IOCs added to the database whithin the past day:
```
python3 threatfox_query_recent-iocs.py 1
```

Pro tip: if you want to stay up to date with the most recent IOCs you may also want to have a look at ThreatFox's [data export](https://threatfox.abuse.ch/export/) which are generated regularely.

## Query IOCs for a given malware family
This script calls ThreatFox's [malware endpoint](https://threatfox.abuse.ch/api/#malware) which returns recent IOCs associated with a certain malware family. The example below shows the 50 most recent IOCs associated with Cobalt Strike
```
python3 threatfox_query_malware.py CobaltStrike 50
```

## Query IOCs associated with a given tag
This script calls ThreatFox's [tag endpoint](https://threatfox.abuse.ch/api/#taginfo) which returns a list of recent IOcs associated with a certain tag. The example below shows the most recent IOCs having the tag "AS_DELIS" set:
```
python3 threatfox_query_tag.py AS_DELIS
```

## Search an IOC
This script calls ThreatFox's [search endpoint](https://threatfox.abuse.ch/api/#search-ioc) which seaches the database for a given IOCs. The example below searches the database for ```ntpjson.monster```:
```
python3 threatfox_search_ioc.py ntpjson.monster
``` 

## Submit an IOC
This script is used to submit IOCs to ThreatFox by calling ThreatFox's [submission endpoint](https://threatfox.abuse.ch/api/#share). Before you submit IOCs to ThreaFox, make sure that you have read our [submission policy](https://threatfox.abuse.ch/api/#policy).

## API documentation

The documentation for the ThreatFox API is available here:

https://threatfox.abuse.ch/api/
