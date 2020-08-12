# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:46:26 2020

@author: felip
"""

""" Importamos todo lo necesario para comenzar """

import pandas as pd
import numpy as np
import random as rnd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

training = pd.read_csv('../dataTitanic/train.csv')
testing = pd.read_csv('../dataTitanic/test.csv')
total = [training, testing]


total.head()