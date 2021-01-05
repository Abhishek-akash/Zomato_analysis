#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
df=file.copy()
df['Aggregate rating'].dropna(inplace=True)
df['Votes'].dropna(inplace=True)
df.reset_index()
res=df.Locality.value_counts()
df['weighted']=df['Aggregate rating']*df['Votes']
print("---------------------***********--------------------------")
print("Top 10 Locality on the basis of Weighted Restaurant Rating ")
print("----------------------------------------------------------")
print((df.groupby("Locality")["weighted"].sum()/df.groupby("Locality")["Votes"].sum()).sort_values(ascending=False)[0:10])


# Numerator=df.groupby('Locality')['weighted'].sum()#Σ (number of votes * rating)
# Denominator=df.groupby('Locality')['Votes'].sum()#Σ (number of votes) 
# res_dict={} #will have the Weighted Restaurant Rating of all Locality
# WRR=[]       
# for i in range(len(Denominator)):
#     WRR.append(round(Numerator[i]/Denominator[i],2))
# #print(WRR)
# for i in range(len(WRR)):
#     res_dict[res.index[i]]=WRR[i]
# sorted_dict=collections.OrderedDict(sorted(res_dict.items(),key=lambda x:x[1],reverse=True))
# print("***------------------------------------------------------***")
# print("Top 10 Locality on the basis of Weighted Restaurant Rating ")
# print("----------------------------------------------------------")
# count=0
# for key,value in sorted_dict.items():
#     if count<10:
#         print(key,"-->",value)
#         count+=1
#     else:
#         break


# In[ ]:




