# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 09:36:41 2019

@author: User
"""
#Scraping Numbers from HTML using BeautifulSoup 
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting 
#numbers and compute the sum of the numbers in the file.
#You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

#Actual data: http://py4e-data.dr-chuck.net/comments_262622.html

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lst = list()
# Retrieve all of the anchor tags
tags = soup('a')
iter = 0
for tag in tags:
    # Look at the parts of a tags
    iter = iter + 1   
    if count != 0 and iter == position:
        print(tag.get('href',None))
        count = count - 1
        position = position * 3 
      

    