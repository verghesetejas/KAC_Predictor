# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:05:48 2018

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