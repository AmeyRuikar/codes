import json
import urllib

serviceURL = "http://python-data.dr-chuck.net/comments_220338.json"

jsonData = urllib.urlopen(serviceURL).read()

js = json.loads(jsonData)

print js

comments = js['comments']

total = 0

for comment in comments:
    
    total = total + int(comment['count'])

print total