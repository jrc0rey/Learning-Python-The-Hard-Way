
import requests
from sys import exit
import json

res = requests.get('https://api.lyrics.ovh/v1/Lynyrd Skynyrd/ Free Bird')

res_json = res.json()

res_json_pretty = json.dumps(res_json, indent=2, sort_keys=True)

print (res_json_pretty)
