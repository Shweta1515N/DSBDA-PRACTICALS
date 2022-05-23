# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:38:35 2022

@author: HP
"""

import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from scipy import stats
df=pd.read_csv("titanic train.csv")
print(df)
col3=df.columns
print(col3)
print(df.info())
print(df.describe())
print(df.isnull().sum())

sns.boxplot(data['sex'],data['age'],data['survied'])
plt.show