# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:14:30 2019

@author: User
"""
#Exploring the HyperText Transport Protocol

#You are to retrieve the intro-short.txt document using the HTTP protocol in a way that you can examine 
#the HTTP Response headers.
#There are three ways that you might retrieve this web page and look at the response headers:

#1) Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to 
#change the code to retrieve the above URL - the values are different for each URL.
#2) Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#3) Use the telnet program as shown in lecture to retrieve the headers and content.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()