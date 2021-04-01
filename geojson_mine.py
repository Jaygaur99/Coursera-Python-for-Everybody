import json
import ssl
import urllib.request, urllib.parse, urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter Location:')
    if len(address)<1:break
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retriving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Reterived',len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None



    print(json.dumps(js,indent=4))
    print('Place ID:',js['results'][0]['place_id'])
