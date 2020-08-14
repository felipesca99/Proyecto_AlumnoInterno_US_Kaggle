# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 19:46:26 2020

@author: felip
"""

""" Importamos todo lo necesario para comenzar """

import pandas as pd
import numpy as np
import random as rnd
import funciones as fn

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

training = pd.read_csv('dataTitanic/train.csv')
testing = pd.read_csv('dataTitanic/test.csv')
total = [training, testing]

"""total_df = pd.DataFrame(total) -> definir pd dataset a través de lista"""

print("Cola y cabeza del entrenamiento")
fn.tails_and_heads(training)
print("Total de casos: "+str(len(training))+"\n\n")

print("Cola y cabeza del testeo")
fn.tails_and_heads(testing)
print("Total de casos: "+str(len(testing))+"\n\n")

print(training.describe())