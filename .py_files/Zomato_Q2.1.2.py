#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
obj=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=obj.copy()
df.fillna('',inplace=True)
def count(list1):
    l=list(list1)
    cuisines=[]
    for i in range(len(l)):
        l[i]=l[i].split(',')
        temp=l[i]
        cuisines.append(len(temp))
    return cuisines
# df.dropna(inplace=True)
aggregate_rating=df['Aggregate rating'].values
number_of_cuisines=list(df.Cuisines)
# print(len(a))
number_of_cuisines=count(number_of_cuisines)
# print(a)
plt.subplots(figsize=(16,6))
plt.scatter(aggregate_rating,number_of_cuisines)
plt.title("Rating Vs Restaurant serving more number of cuisines.").set_color('r')
plt.xlabel('rating').set_color('r')
plt.show()


# In[ ]:




