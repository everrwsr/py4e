import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1630197.xml'



print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

comments_node = tree.findall('comments')
comment_node = comments_node[0].findall('comment')

total = 0
for node in comment_node:
    total = total + int(node.find('count').text)
print(total)