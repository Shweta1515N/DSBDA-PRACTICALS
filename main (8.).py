import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\HP\seaborn-data\titanic.csv")

sns.distplot(data['Fare'])
plt.show()

sns.jointplot(x="Sex",y="Fare",data=data)
plt.show()

sns.rugplot(data["Fare"])
plt.show()

sns.pairplot(data)
plt.show()