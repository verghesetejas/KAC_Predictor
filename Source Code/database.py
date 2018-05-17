# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 17:06:17 2018

    KAC Predictor (Key-Agricultural Commodities Daily Market Price Prediction using Deep Neural Networks)
    Copyright (C) 2018  Tejas Verghese

    This file is part of KAC Predictor.

    KAC Predictor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    KAC Predictor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with KAC Predictor.  If not, see <http://www.gnu.org/licenses/>.

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