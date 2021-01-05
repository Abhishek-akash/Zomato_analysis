#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
res=df.groupby('Restaurant Name')['Votes'].sum().sort_values(ascending=False)[0:10]
name=res.index
value=res.values
x=plt.bar(name,value)

plt.title("Top 10 Restaurant with most number of votes").set_color('r')
plt.xticks(rotation=90)
plt.show()

