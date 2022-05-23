# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:50:59 2022

@author: DELL
"""

import pandas as pd
import numpy as np
df=pd.read_csv("StudentPerformance.csv")
print(df.notnull())

print(df.isnull())
series1 = pd.isnull(df["math score"])
print(df[series1])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
newdf=df
print(df)

m_v=df['math score'].mean()
df['math score'].fillna(value=m_v, inplace=True)
print(df)

missing_values = ["Na", "na"]
df = pd.read_csv("StudentPerformance.csv", na_values =missing_values)
print(df)

