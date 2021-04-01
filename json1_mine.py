import json
import urllib.request , urllib.error, urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = input("Enter location:")
print('Retrieving:',fhand)
fh = urllib.request.urlopen(fhand,context = ctx)
data = fh.read().decode()
print('Reterived',len(data),'characters')
js = json.loads(data)
sum = 0
count = 0
for item in js['comments']:
    c = int(item['count'])
    sum = sum + c
    count += 1
print('Count:',count)
print('Sum:',sum)
