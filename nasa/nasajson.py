import json
import requests
url="https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"
response = requests.get(url)
d= response.json()
with open('nasa.json','w') as outfile :
    json.dump(d,outfile, indent=4)
