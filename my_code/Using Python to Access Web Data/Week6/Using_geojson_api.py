# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:30:52 2019

@author: User
"""
#Calling a JSON API

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
#and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as 
#within Google Maps.

#API End Points
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as
#you like. If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to provide the address that you are requesting as the address= parameter that is properly URL
#encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

import urllib.request,urllib.parse,urllib.error
import ssl
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address)<1:break
    parms = dict()
    parms['address']=address
    if api_key is not False:
        parms['key']=api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh = urllib.request.urlopen(url,context=ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'charactesr')    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK':
        print('====Failure to retrieve====')
        print(data)
        continue

    
    place_id = js['results'][0]['place_id']
    print('Place id',place_id)
    

    