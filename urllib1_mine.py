import re
import urllib
from bs4 import BeautifulSoup

html = urnlib.urlopen('http://py4e-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(htmp,"html.parser")

tags = soup('span')
for tag in tags:
    y = str(tag)
    x = re.findall("[0-9]+",y)
    print(x)
