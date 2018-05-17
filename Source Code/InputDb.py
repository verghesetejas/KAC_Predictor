# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:54:31 2018

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