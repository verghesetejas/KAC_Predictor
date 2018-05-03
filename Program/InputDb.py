# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:54:31 2018

@author: Tejas Verghese
"""

'''
import sqlite3

###  TableName:: INPUT  ###
connection = sqlite3.connect("combo_loader.db")
connection.execute("CREATE TABLE INPUT(STATE TEXT NOT NULL, DISTRICT TEXT, MARKET TEXT NOT NULL, COMMODITY TEXT NOT NULL, DATE TEXT NOT NULL)")
connection.commit()
connection.close()


###  TableName:: OUTPUT  ###
connection = sqlite3.connect("combo_loader.db")
connection.execute("CREATE TABLE OUTPUT(STATE TEXT NOT NULL, DISTRICT TEXT, MARKET TEXT NOT NULL, COMMODITY TEXT NOT NULL, DATE TEXT NOT NULL, MIN_PRICE REAL NOT NULL, MAX_PRICE REAL NOT NULL, MOD_PRICE REAL NOT NULL)")
connection.commit()
connection.close()
'''