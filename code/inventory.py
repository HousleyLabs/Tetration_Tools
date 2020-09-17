""""
Sample Code - Housley Communications
-Inventory Search
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
search_query = {
    "scopeName" : "Housley",
    "limit" : 15,
    "filter": {
        "type" : "or",
        "filters": [
            {
                "type": "contains",
                "field": "hostname",
                "value": "p17"
            },
            {
                "type": "subnet",
                "field": "ip_address",
                "value": "172.18.17.0/24"
            }
        ]
    }
}

inventory = client.post('/inventory/search', json_body=json.dumps(search_query))

# Convert Text to json
json_output=json.loads(inventory.text)

# print Json in format output
pprint(json_output)
