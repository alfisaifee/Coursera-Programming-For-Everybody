# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:46:49 2019

@author: User
"""
#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

#The basic outline of this problem is to read the file, look for integers using the re.findall(), 
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers 
#and summing up the integers.

import re
fname = r'\Users\User\Desktop\New folder (2)\re_sum.txt'
fh = open(fname)
lst = list()
add = 0
for line in fh:
    line = line.strip()
    numfind = re.findall('[0-9]+',line)
    if len(numfind) >= 1:
        lst.extend(numfind)

for n in lst:
    add = add + int(n)

print(lst)    
print(add)    




