# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 08:45:39 2019

@author: User
"""

#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the 
#comment counts from the XML data, compute the sum of the numbers in the file.
#http://py4e-data.dr-chuck.net/comments_262624.xml

import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print('Retrieving ',url)
fhand = urllib.request.urlopen(url,context = ctx).read()
print('Retrieved', len(fhand), 'characters')
tree = ET.fromstring(fhand)
comments = tree.findall('comments/comment')
lst = list()
for item in comments:
    lst.append(item.find('count').text)

add = 0
for e in lst:
    add = add + int(e)

print('Count:',len(lst))
print('Sum:',add)
    
