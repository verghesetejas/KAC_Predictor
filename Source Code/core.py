'''
-*- coding: utf-8 -*-

Created on Mon Mar 19 22:22:12 2018

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
'''

'''
# importing necessary libraries
import numpy as np
import pandas as pd
import datetime as DT
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MaxAbsScaler
from sklearn.externals import joblib
# Import keras libraries
from keras.models import Sequential, load_model
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor


# Part I - Data Preprocessing

# Importing the dataset
fileName = '../Datasets/KAC_training.csv'
dataset = pd.read_csv(fileName)
dataset.columns = [0, 1, 2, 3, 4, 5, 6, 7]
dataset[4] = pd.to_datetime(dataset[4], format='%d/%m/%Y').dt.date
dataset[4] = dataset[4].map(DT.datetime.toordinal)
dataset[5] = np.vstack(dataset[5]).astype(np.float)
dataset[6] = np.vstack(dataset[6]).astype(np.float)
dataset[7] = np.vstack(dataset[7]).astype(np.float)

# Splitting Dataset to adjust Missing values
# Also, X will be the Independent variable dataset
X = pd.DataFrame(dataset.iloc[:, :-3].values)
y = pd.DataFrame(dataset.iloc[:, 5:8].values)

# Taking care of Missing Data
imputer = Imputer(missing_values=0, strategy='most_frequent', axis=0)
imputer = imputer.fit(y[:])
y[:] = imputer.transform(y[:])

# Splitting Dataset's 3 Dependent variables - Min_Price, Max_Price and Modal_Price
y_min = pd.DataFrame(y.iloc[:, 0].values)
y_max = pd.DataFrame(y.iloc[:, 1].values)
y_mod = pd.DataFrame(y.iloc[:, 2].values)

# Categorical Data
leX_state = LabelEncoder()
leX_district = LabelEncoder()
leX_market = LabelEncoder()
leX_commodity = LabelEncoder()
X[0] = leX_state.fit_transform(X[0])
X[1] = leX_district.fit_transform(X[1])
X[2] = leX_market.fit_transform(X[2])
X[3] = leX_commodity.fit_transform(X[3])
np.save('leX_state.npy', leX_state.classes_)
np.save('leX_district.npy', leX_district.classes_)
np.save('leX_market.npy', leX_market.classes_)
np.save('leX_commodity.npy', leX_commodity.classes_)

# Splitting the dataset into training set and test set
# KAC_MaxModel
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y_mod,
                                                    test_size = 0.2,
                                                    random_state = 0)

# Feature Scaling
sc_X = MaxAbsScaler()
sc_y = MaxAbsScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
y_train = sc_y.fit_transform(y_train)
y_test = sc_y.transform(y_test)
joblib.dump(sc_X, 'sc_X.pkl')
joblib.dump(sc_y, 'sc_y_mod.pkl')

# Extra
sc_X = MaxAbsScaler()
sc_X = joblib.load('sc_X.pkl')
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Part II - Deep Neural Network Model

# KAC Model Architecture
def kac_model():
    # Create object of the Sequential Class
    model = Sequential()
    # Adding the Input Layer and the First Hidden Layer
    model.add(Dense(5, input_dim = 5, kernel_initializer = 'normal', activation = 'tanh'))
    # Adding the Second Hidden Layer
    model.add(Dense(3, kernel_initializer = 'normal', activation = 'tanh'))
    # Adding the Output Layer
    model.add(Dense(1, kernel_initializer = 'normal'))
    # Compiling the model
    model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics=['acc', 'mean_squared_error'])
    # returning the Model
    return model

# Creating a Regression Model
estimator = KerasRegressor(build_fn=kac_model, nb_epoch=100, batch_size=10, verbose=0)
estimator.fit(X_train, y_train)

# Predicting the Values
y_new = estimator.predict(X_test)
y_pred = sc_y.inverse_transform(estimator.predict(X_test).reshape(-1, 1))
y_test = sc_y.inverse_transform(y_test)

# Saving the KAC Model
estimator.model.save('KAC_ModModel.h5')

# Deleting current Model
del estimator

# Loading saved Model
predictor = load_model('KAC_ModModel.h5')

# Evaluate the Model
score = predictor.evaluate(X_train, y_train, verbose=0)
print("%s: %.2f%%" % (predictor.metrics_names[1], score[1]*100))
'''