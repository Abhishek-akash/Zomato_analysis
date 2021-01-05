#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
file=pd.read_csv(r'/Users/abhishek.kumar13027/Downloads/zomato.csv')
df=file.copy()
df.plot.scatter(x='Aggregate rating',y='Votes',figsize=(10,6), color='orange', title="Agg Rating vs Votes")
plt.grid()
plt.show()
print('In general trend more number of votes signify restaturant provide good serivice')
print('From the graph we can see that if Number of votes is greater than 4500 then restaurant rating lie between 3.5-5.0')
print('If Number of Votes is greater tahn 6000 then restaurant rating lie between 4.3-5')
print("More number of votes means more rating")


# In[ ]:




