# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:53:03 2019

@author: User
"""

#Following Links in Python

#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the
#process a number of times and report the last name you find.

#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_James.html 
#Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
#The answer is the last name that you retrieve.


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL :')

count = int(input('Enter count : '))
position = int(input('Enter position : '))
while count != 0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
`   tags = soup("a")
    iter = 1
    for tag in tags:
        if iter == position:
            url = tag.get('href',None)
            print(url) 
        iter += 1    
    count -= 1
                