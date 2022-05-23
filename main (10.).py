import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

#head = ['seapl_length','seapal_width','petal_lentg','petal_width']

data = pd.read_csv("D:\Documents\DSBDA Program\practical 1\Iris.csv")
print(data)

sns.distplot(data['SepalLengthCm'],bins=20)

plt.show()

sns.distplot(data['SepalWidthCm'],bins=20)
plt.show()

sns.distplot(data['PetalLengthCm'],bins=20)
plt.show()

sns.distplot(data['PetalWidthCm'],bins=20)
plt.show()

sns.boxplot(data["PetalLengthCm"])
plt.show()

fig=plt.figure(1,figsize=(12,8))
dataset=[data["SepalLengthCm"],data["SepalWidthCm"],data["PetalLengthCm"],data["PetalWidthCm"]]
fig.add_subplot(111).boxplot(dataset)
plt.show()