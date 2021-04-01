from urllib.request import urlopen
import re
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)
