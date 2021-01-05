#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
res=df['Restaurant Name'].value_counts().sort_values(ascending=False)[0:15]
name=res.index
value=res.values
print("top 15 restaurants have a maximum number of outlets")
print(res)
plt.bar(name,value)
plt.title("top 15 restaurants have a maximum number of outlets").set_color('r')
plt.ylabel('Outlets').set_color('r')
plt.xticks(rotation=90)
plt.show()


# In[ ]:




