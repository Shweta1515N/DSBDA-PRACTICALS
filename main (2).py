import pandas as pd
import numpy as np

na_val=["na","Nan","None","Na"]
data=pd.read_csv("D:\Documents\DSBDA Program\practical no 2\data.csv",na_values=na_val)

sortdata=sorted(data['aptitude'])

q1=np.percentile(sortdata,25)
q3=np.percentile(sortdata,75)
iqr=q3-q1
low=q1-(iqr*1.5)
high=q3+(iqr*1.5)

length=len(data.index)
for i in range(0,length):
    if(data['aptitude'][i]<low):
        data['aptitude'][i]=data['aptitude'].mode()

wrt_val=data['write'].mode()
ndf=data
ndf=ndf.dropna()
print(ndf)
