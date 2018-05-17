#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:47:08 2018

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

import numpy as np
import pandas as pd
import datetime as DT
import sqlite3
from sklearn.preprocessing import LabelEncoder
from sklearn.externals import joblib
# Import keras libraries
from keras.models import load_model

class KAC_Predictor:
    checkPoint = 0
    
    def loadMinModel(self):
        return load_model('KAC_MinModel.h5')
    
    def loadMaxModel(self):
        return load_model('KAC_MaxModel.h5')
    
    def loadModModel(self):
        return load_model('KAC_ModModel.h5')
    
    def loadDataset(self):
        # Loading the dataset
        connection = sqlite3.connect("combo_loader.db")
        dataset = pd.read_sql_query("SELECT * FROM INPUT", connection)
        connection.close()
        dataset.columns = [0, 1, 2, 3, 4]
        dataset[4] = pd.to_datetime(dataset[4], format='%d/%m/%Y').dt.date
        dataset[4] = dataset[4].map(DT.datetime.toordinal)
        
        # Categorical Data
        leX_state = LabelEncoder()
        leX_state.classes_ = np.load('leX_state.npy')
        leX_district = LabelEncoder()
        leX_district.classes_ = np.load('leX_district.npy')
        leX_market = LabelEncoder()
        leX_market.classes_ = np.load('leX_market.npy')
        leX_commodity = LabelEncoder()
        leX_commodity.classes_ = np.load('leX_commodity.npy')
        dataset[0] = leX_state.fit_transform(dataset[0])
        dataset[1] = leX_district.fit_transform(dataset[1])
        dataset[2] = leX_market.fit_transform(dataset[2])
        dataset[3] = leX_commodity.fit_transform(dataset[3])
        
        # Feature Scaling
        self.sc_X = joblib.load('sc_X.pkl')
        self.X = self.sc_X.fit_transform(dataset)


        
    def predictor(self):
        minModel = self.loadMinModel()
        maxModel = self.loadMaxModel()
        modModel = self.loadModModel()
        self.loadDataset()
        
        self.sc_y_min = joblib.load('sc_y_min.pkl')
        self.sc_y_max = joblib.load('sc_y_max.pkl')
        self.sc_y_mod = joblib.load('sc_y_mod.pkl')
        
        y_min_pred = self.sc_y_min.inverse_transform(minModel.predict(self.X).reshape(-1, 1))
        y_max_pred = self.sc_y_max.inverse_transform(maxModel.predict(self.X).reshape(-1, 1))
        y_mod_pred = self.sc_y_mod.inverse_transform(modModel.predict(self.X).reshape(-1, 1))
        
        connection = sqlite3.connect("combo_loader.db")
        dataset = pd.read_sql_query("SELECT * FROM INPUT", connection)
                
        df1 = pd.DataFrame(y_min_pred)
        df2 = pd.DataFrame(y_max_pred)
        df3 = pd.DataFrame(y_mod_pred)
        dataset = pd.concat([dataset, df1, df2, df3], axis=1)
        dataset.columns = ['STATE', 'DISTRICT', 'MARKET', 'COMMODITY', 'DATE', 'MIN_PRICE', 'MAX_PRICE', 'MOD_PRICE']
        
        connection.execute("DELETE FROM OUTPUT")
        dataset.to_sql(name='OUTPUT', con=connection, if_exists='append', index=False)
        connection.execute("UPDATE OUTPUT SET MIN_PRICE = ABS(MIN_PRICE), MAX_PRICE = ABS(MAX_PRICE), MOD_PRICE = ABS(MOD_PRICE) WHERE MIN_PRICE<0 OR MAX_PRICE<0 OR MOD_PRICE<0")
        connection.execute("UPDATE OUTPUT SET MIN_PRICE = ROUND(MIN_PRICE), MAX_PRICE = ROUND(MAX_PRICE), MOD_PRICE = ROUND(MOD_PRICE)")
        connection.commit()
        connection.close()
        self.checkPoint = 1