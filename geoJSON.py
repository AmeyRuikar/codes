import json
import urllib

serviceURL = "http://python-data.dr-chuck.net/geojson?"

url = serviceURL + urllib.urlencode({'sensor':'false', 'address': 'University of Pennsylvania'})

data = urllib.urlopen(url).read()

jdata = json.loads(data)

print jdata['results'][0]['place_id']