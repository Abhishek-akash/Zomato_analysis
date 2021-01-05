#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
df.plot.scatter(x='Aggregate rating',y='Average Cost for two',figsize=(10,6), color='blue', title="Agg Rating vs Avg Cost")
plt.grid()
plt.show()

print('From the graph we can see that if avg cost is less the rating differ from (0-4.8) ')
print('If avg cost is higher then restaurant rating lie between 3.5 to 4.8')
print("we can conclude that rest will surely have higher rating if its avg cost is higher")


# In[ ]:




