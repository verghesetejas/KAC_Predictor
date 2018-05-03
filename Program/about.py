# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:50:24 2018

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
        webbrowser.open_new(r'Major Project Report - Tejas Verghese.pdf')