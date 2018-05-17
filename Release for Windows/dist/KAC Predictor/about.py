# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:50:24 2018

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

import webbrowser

# This Opens The PDF file which shows the Details of the Developers
class AboutDeveloper:

    def __init__(self):
        webbrowser.open_new(r'AboutDeveloper.pdf')

# This Opens The PDF file which shows the Details of the Project       
class AboutProject:
    
    def __init__(self):
        webbrowser.open_new(r'AboutProject.pdf')