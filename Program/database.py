# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:06:17 2018

@author: Tejas Verghese
"""

'''
import sqlite3

def createTable():
    connection = sqlite3.connect("login.db")
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT NOT NULL)")
    connection.execute("INSERT INTO USERS VALUES(?,?,?)", ('verghesetejas', 'verghesetejas@gmail.com', 'MajorProject@2018'))
    connection.commit()
    result = connection.execute("SELECT * FROM USERS")
    for data in result:
        print("Username: ", data[0])
        print("Email: ", data[1])
        print("Password: ", data[2])
    connection.close()

createTable()
'''