# -*- coding: utf-8 -*-

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.request

url = 'http://awesome-linus.tk/wp-content/uploads/2017/08/cropped-cropped-seashore.jpg'

getimage = url.split('/')[-1]

req = Request(url)

try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    urllib.request.urlretrieve(url, getimage)
    print("File Saved as '" + getimage + "'")
