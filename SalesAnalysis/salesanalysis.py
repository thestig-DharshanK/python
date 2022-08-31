import pandas as pd
from datetime import datetime
from collections import Counter
from itertools import combinations
import os
l=[]
files=[file for file in os.listdir("SalesAnalysis\Sales_Data") ]
print(files)
all=pd.DataFrame()
for i in files:
    f=pd.read_csv("SalesAnalysis/Sales_Data/"+i)
    all=pd.concat([f,all])
all.reset_index(drop=True,inplace=True)
format="%m/%d/%y %H:%M"
for i in all['Order Date']:
    try:
      l.append(datetime.strptime(i,format))
    except:
        l.append("N/A")
all['Order Date']=l
m=[]
for i in all['Order Date']:
    try:
        m.append(i.strftime("%B"))
    except:
        m.append(i)
all['month']=m
all=all.drop(all[all["Order Date"]=="N/A"].index)
all.reset_index(drop=True,inplace=True)
print(all.columns)
all['Price Each']=all['Price Each'].astype("float")
all['Quantity Ordered']=all['Quantity Ordered'].astype("float")
all['sales']=all['Quantity Ordered']*all['Price Each']
a=all.groupby(['month']).sum()
print(a.index[a['sales']==a['sales'].max()])
all['hour']=[i.strftime("%H") for i in all['Order Date']]
all['minute']=[i.strftime("%M") for i in all['Order Date']]
hrs=[h for h,df in all.groupby("hour")]
print(hrs)
df=all[all['Order ID'].duplicated(keep=False)]
df['group']=df.groupby(['Order ID'])['Product'].transform(lambda x: ','.join(x))
df=df[['Order ID','group']].drop_duplicates()
print(df)
df.to_csv("df.csv")
c=Counter()
for i in df['group']:
    a=i.split(",")
    c.update(Counter(combinations(a,2)))
print(c)
print(c.most_common(10))





