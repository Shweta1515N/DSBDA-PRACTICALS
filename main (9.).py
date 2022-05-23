import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Documents\DSBDA Program\practical 8\titanic.csv")

sns.boxplot(data['Sex'],data['Age'])
plt.show()

sns.boxplot(data['Sex'],data['Age'],data['Survived'])
plt.show()