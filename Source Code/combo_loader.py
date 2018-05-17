# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:59:32 2018

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
# Import Libraries
import pandas as pd
import sqlite3

# Prepare DataFrame to export to SQLite3
fileName = 'TrainingDataset.csv'
fileName_2 = 'TrainingDataset_2.csv'
csv = pd.read_csv(fileName)
csv_2 = pd.read_csv(fileName_2)
csv = csv.append(csv_2, ignore_index = True)
df = pd.DataFrame(csv.iloc[:, :4].values)
df.columns = ['STATE', 'DISTRICT', 'MARKET', 'COMMODITY']

# Create a New Table combo_loader.db
connection = sqlite3.connect("combo_loader.db")
connection.execute("CREATE TABLE BOX(STATE TEXT NOT NULL, DISTRICT TEXT, MARKET TEXT NOT NULL, COMMODITY TEXT NOT NULL)")
df.to_sql(name='BOX', con=connection, if_exists='append', index=False)
connection.commit()

# Checking the SQLite3 table for values
result = connection.execute("SELECT * FROM BOX")
count=5
for data in result:
    if count>=0:
        print("State: ", data[0])
        print("District: ", data[1])
        print("Market: ", data[2])
        print("Commodity: ", data[3])
        count=count-1
connection.close()
'''