# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:12:16 2019

@author: User
"""
#Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
#the comment counts from the JSON data, compute the sum of the numbers in the file.
#Actual data: http://py4e-data.dr-chuck.net/comments_262625.json

import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving',url)
fhand = urllib.request.urlopen(url).read()
print('Retrieved',len(fhand),'characters')
lst = list()
data = json.loads(fhand)

for item in data['comments']:
    lst.append(item['count'])
print('Count:',len(lst))
print('Sum:',sum(lst))    