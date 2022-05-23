import pandas as pd

read=pd.read_csv("D:\Documents\DSBDA Program\practical no 3\data.csv")
#Print Unique
print(read.age_group.unique())

#Group BY min
print(read.groupby(read.age_group).min())

#Group BY max
print(read.groupby(read.age_group).max())

#Group by mean
print(read.groupby(read.age_group).mean())

#Group by std
print(read.groupby(read.age_group).std())

#Group by count
print(read.groupby(read.age_group).count())