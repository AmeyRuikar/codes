import xml.etree.ElementTree as ET
import urllib

serviceURL = "http://python-data.dr-chuck.net/comments_220334.xml"

connect = urllib.urlopen(serviceURL)
data = connect.read()

print data

tree = ET.fromstring(data)

# don't start from anchor tag
result = tree.findall('comments/comment')

print result

sum2 = 0

for comment in result:
    x = int(comment.find('count').text)
    print x
    sum2 = sum2 + x
    
print sum2