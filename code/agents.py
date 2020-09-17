""""
Sample Code - Housley Communications
- Agent/Sensor list
These APIs are only available to site admin users.
"""
from tetpyclient import RestClient
import requests.packages.urllib3
from pprint import pprint
import json

# set variables
server = "oz.tet.hl.dns"
creds  = "./api_credentials.json"

# open connection class
client = RestClient(server, credentials_file=creds, verify=False)

# suppress warning message
requests.packages.urllib3.disable_warnings()

# GET the list of agents
sensors = client.get('/sensors')

# Convert Text to json
json_output=json.loads(sensors.text)

# print Json in format output
pprint(json_output)
