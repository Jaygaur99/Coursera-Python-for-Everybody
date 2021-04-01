import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count: "))
ipos =  int(input('Enter position: '))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
pos = 0
lst = list()
while count > 0:
    tags = soup('a')
    for tag in tags:
        link = tag.get('href',None)
        lst.append(link)
    print('Retrieving: ',lst[pos + ipos])
    url = lst[pos + ipos]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    pos = pos + 100
    count -=1
