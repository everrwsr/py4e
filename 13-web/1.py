from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url= input(' enter ---')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')


tags = soup('li')
for tag in tags:
    print(tag.get('href',None))