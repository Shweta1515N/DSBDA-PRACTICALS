import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = load_boston()

data = pd.DataFrame(dataset.data,columns=dataset.feature_names)

data["Price"] = dataset.target

print(data.describe())

print(data.info())

sns.displot(data["Price"])
plt.show() 

plt.scatter(data['LSTAT'],data["Price"])
plt.xlabel("Price")
plt.ylabel("LSTAT")
plt.show()

x = pd.DataFrame(np.c_[data['LSTAT'],data["RM"]],columns=["LSTAT","RM"])
y = data["Price"]

x_train,x_test,y_train,y_test=train_test_split(x,y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

model = LinearRegression()
model.fit(x_train,y_train)

price = model.predict([[12.65,6.8]])
print(price)