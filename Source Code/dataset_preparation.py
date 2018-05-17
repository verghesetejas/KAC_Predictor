# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:05:48 2018

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
# importing necessary libraries
import pandas as pd

# Importing the dataset
fileName = 'TrainingDataset.csv'
fileName_2 = 'TrainingDataset_2.csv'
csv = pd.read_csv(fileName)
csv_2 = pd.read_csv(fileName_2)
csv = csv.append(csv_2, ignore_index = True)

# Editing the Dataset
df1 = pd.DataFrame(csv.iloc[:, :4].values)
df2 = pd.DataFrame(csv.iloc[:, 5:].values)
dataset = pd.concat([df1, df2], axis = 1)
dataset.columns = ['State',
                   'District',
                   'Market',
                   'Commodity',
                   'Arrival_Date',
                   'Min_Price',
                   'Max_Price',
                   'Modal_Price']

# Exporting the dataset to csv
dataset.to_csv(path_or_buf='D:\MajorProject\Datasets\KAC_training.csv', index=False, chunksize=100000)
'''