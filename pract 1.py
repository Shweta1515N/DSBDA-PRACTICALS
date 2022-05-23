# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:56:17 2022

@author: DELL
"""

import numpy as np
import pandas as pd 
iris = pd.read_csv("iris.data", header = None)
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
iris = pd.read_csv("iris.data", names = col_names)

print(iris.head())

print(iris.head(n=5))

print(iris.tail(n=5))

print(iris.index)

print(iris.columns )

print(iris.shape)

print(iris.dtypes)

print(iris.columns.values )

print(iris.describe(include='all'))

print(iris[col_names])
           
print(iris.sort_index(axis=1,ascending=False))

print(iris.sort_values(by=col_names))

print(iris.iloc[5])
print(iris[0:3])
#print(iris.loc[:, ["col_name1","col_name2"]])
#print(iris.iloc[:n, :])

#print(iris.iloc[:, :n])
print(iris.iloc[3:5, 0:2]) 
print(iris.dtypes)