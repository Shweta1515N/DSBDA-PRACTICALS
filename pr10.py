# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:58:38 2022

@author: HP
"""
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
%matplotlib inline
from scipy import stats
df=pd.read_csv("iris.csv",header=None)
df.columns=["col1","col2","col3","col4","col5"]
print(df.head())
column=len(list(df))
print(column)
print(df.info())
print(np.unique(df["col5"]))

fig, axes=plt.subplots(2,2,figsize=(16,8))

axes[0,0].set_title("Distrubution of first column")
axes[0,0].hist(df["col1"]);


axes[0,1].set_title("Distrubution of second column")
axes[0,1].hist(df["col2"]);

axes[1,0].set_title("Distrubution of third column")
axes[1,0].hist(df["col3"]);

axes[1,1].set_title("Distrubution of fourth column")
axes[1,1].hist(df["col4"]);