#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')

df=file.copy()
df['Aggregate rating'].dropna(inplace=True)
df.reset_index()
rat=df['Aggregate rating'].value_counts().index
res=df['Aggregate rating'].sort_values(ascending=False)
l1=[]
for i in rat:
    l1.append(i)
l1.sort()
#print(l1)

plt.hist(res,bins=[0,1,2,3,4,4.5,4.8,4.9],color='y',edgecolor='black')
plt.title("Histogram of aggregate rating of Restaurants").set_color('r')
plt.xlabel("Rating").set_color('r')
plt.ylabel("Frequency").set_color('r')
plt.xticks([0,1,2,2.5,2.8,3,3.5,3.8,4,4.5,4.9],rotation=90)
plt.show()


# In[ ]:




