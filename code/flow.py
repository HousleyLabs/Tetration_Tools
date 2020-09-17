""""
Sample Code - Housley Communications
- Flow Search script

set filters for:
- max 24 hr time range
- number of records returned
- destination port
- destination host name contains
- source Subnet
"""

from tetpyclient import RestClient
import requests.packages.urllib3
from pprint import pprint
import json

# set variables
server = "https://oz.tet.hl.dns"
creds  = "./api_credentials.json"

# open connection class
client = RestClient(server, credentials_file=creds, verify=False)

# suppress warning message
requests.packages.urllib3.disable_warnings()

# Set Query value
# T0(start) and T1(end) format is Date: yyyy-mm-dd, Time:hh:mm:offset as (+-)hh:mm
# https://en.wikipedia.org/wiki/ISO_8601

# note: the time range is a maximum of 1 day

search_query = {
    "scopeName" : "Housley:Tenant17",
    "t0": "2020-09-17T00:00:00+1000",
    "t1": "2020-09-17T23:59:59+1000",
    "limit": 5,
    "filter": {
        "type" : "and",
        "filters": [
                        {
                "type": "in",
                "field": "dst_port",
                "values": ["80"]
            },
            {
                "type": "subnet",
                "field": "src_address",
                "value": "172.18.17.0/24"
            },

            {
                "type": "contains",
                "field": "dst_hostname",
                "value": "oc"
            }
        ]
    }
}


# display query for debug - uncomment next line
# pprint(search_query)



# send query to get flows
flows = client.post('/flowsearch', json_body=json.dumps(search_query))

# check http return code = looking for a 200
# 400 family is a malformed request - check JSON
print("HTTP return code: %s "  %(flows.status_code))

# add some error handling to check processing was ok
try:
    # Convert Text to json
    json_output=json.loads(flows.text)

        # print Json in format output
    pprint(json_output)

except:
    print(" ** Issue with request \n ** No output returned ")
