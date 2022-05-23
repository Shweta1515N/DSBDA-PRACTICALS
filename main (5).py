import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix ,precision_score

data = pd.read_csv("D:\Documents\DSBDA Program\practical 5\Social_Network_Ads.csv")


plt.scatter(data['Age'],data["Purchased"])
plt.xlabel("Age")
plt.ylabel("Purchased")
plt.show()

#Split the data set
x_train,x_test,y_train,y_test=train_test_split(data["Age"],data['Purchased'])

#create the Model
model=LogisticRegression()
model.fit(x_train.values.reshape(-1,1),y_train.values.reshape(-1,1).ravel())

y_pred=model.predict(x_test.values.reshape(-1,1)).ravel()

plt.scatter(x_test,y_pred)
plt.show()

tn,fp,fn,tp=confusion_matrix(y_test,y_pred).ravel()
print(tn)
print(fp)
print(fn)
print(tp)

print()
print(precision_score(y_test,y_pred))

