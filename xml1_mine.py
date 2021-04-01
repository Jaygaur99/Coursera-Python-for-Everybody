import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET

fhand = input('Enter url: ')
fh = urllib.request.urlopen(fhand).read()

sum = 0
tree = ET.fromstring(fh)
for comments in tree.findall('comments'):
    for comment in comments.findall('comment'):
        sum = sum + int(comment.find('count').text)
print(sum)
