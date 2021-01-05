#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
af=df[df['Country Code']==216]
res=af.Cuisines.value_counts().index
l1_cuisine=[]

for i in res:
    sep_list=i.split(',')
    if len(sep_list)>1:
        for j in sep_list:
            l1_cuisine.append(j.strip())
    else:
        l1_cuisine.append(sep_list[0].strip())
usa_dict={}
for i in set(l1_cuisine):
    usa_dict[i]=l1_cuisine.count(i)
cuisine_sorted_dict=collections.OrderedDict(sorted(usa_dict.items(),key=lambda x:x[1],reverse=True))
count=0
name=[]
values=[]
for key,value in cuisine_sorted_dict.items():
    if count<10:
        name.append(key)
        values.append(value)
        count+=1
    else:
        break
#print(values)
plt.pie(values,labels=name,autopct='%.2f')
plt.axis('equal')
plt.show()

