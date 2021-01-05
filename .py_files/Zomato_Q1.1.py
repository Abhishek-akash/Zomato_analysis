#!/usr/bin/env python
# coding: utf-8

# In[14]:


#import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
#print(pwd)
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
af=df[df['Country Code']==1]
IndianCity_count=af.City.value_counts().sum()
print("total restaurant in indian cities-->",IndianCity_count)
df=df[(df['City']=='New Delhi')|(df['City']=='Ghaziabad')|(df['City']=='Noida')|(df['City']=='Gurgaon')|(df['City']=='Faridabad')]
DelhiNCR_count=df.City.value_counts().sum()
print("total restaurant in Delhi-Ncr Delhi-NCR-->",DelhiNCR_count)
print("Total restaurant in rest of india-->",IndianCity_count-DelhiNCR_count)
y_city=["Delhi-NCR","Rest Indian Cities"]
x_Counts=[DelhiNCR_count,IndianCity_count-DelhiNCR_count]
plt.rcParams["figure.figsize"] = (6,3)
plt.bar(y_city,x_Counts,width=0.2)
# plt.xlabel("City").set_color('r')
# plt.ylabel("Weighted Restaurant Rating").set_color('r')
plt.title("Number of restaurant in indian cities",c='r')
#plt.axis('equal')
plt.xticks(rotation=20)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




