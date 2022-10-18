import urllib
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    url = input('Enter location: ')
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
    if len(url) < 1 : break
    print('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read()
    print('Retrieved',len(data),'characters')

    tree = ET.fromstring(data)

    allNode = tree.findall('.//count')

    print('count: ', len(allNode))

    sum = 0
    for node in allNode:

        number = int(node.text)
        sum = sum + number

    print('sum:', sum)

    break