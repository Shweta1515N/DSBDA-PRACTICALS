
import pandas as pd
import numpy as np
from sklearn import preprocessing

#Load the dataset
df = pd.read_csv("C:\Users\HP\Desktop\Iris.csv")
print(df)

#Data Preprocessing:check for missing value using (isnull())
print(df.isnull())

#is there any missing values across each column
print(df.isnull().any())

#count row wise missing value using isnull()
print(df.isnull().sum(axis=1))

#count Column wise missing value using isnull()
print(df.isnull().max())

#describe() function to get some initial statistics
print(df.describe())

#Data Formatting and Data Normalization
print(df.dtypes)

df['SepalLengthCm']= df['SepalLengthCm'].values.astype(str)

print(df)

le = preprocessing.LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])
print(df)


