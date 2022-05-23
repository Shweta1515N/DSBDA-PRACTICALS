import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score,precision_score,recall_score

data=pd.read_csv("D:\Documents\DSBDA Program\practical no 6\Iris.csv")
 
# print(data.describe())

# print(data.info())

#Data Preparation Phase
x=data.iloc[:,:4]
y=data["Species"]

#data Spliting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#model Create
model=GaussianNB()
model.fit(x_train,y_train)

#prediction Phase
y_pred=model.predict(x_test)

print(y_pred)

#Accuracy
print(accuracy_score(y_test,y_pred))
print(recall_score(y_test,y_pred,average='micro'))


