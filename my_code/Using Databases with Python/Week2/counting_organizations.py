# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:42:48 2019

@author: User
"""
#Counting Organizations
#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
#(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

import re
import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
url = r'\Users\User\Desktop\Coursera PFE\my_code\Using Databases with Python\Week2\mbox.txt'
fhand = open(url)
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        org = re.findall('(?<=@).*$',line)[0]
        cur.execute('SELECT Count from Counts WHERE org= ?',(org,))
        row = cur.fetchone()-
        if row is None:
            cur.execute('INSERT INTO Counts(org,count) VALUES(?,1)',(org,)) 
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
        conn.commit()
            
sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
    
cur.close()    