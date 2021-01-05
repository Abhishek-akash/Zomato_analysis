#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import os
import collections
import matplotlib.pyplot as plt
#print(pwd)
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
zomato_data=file.copy()
zomato_india=zomato_data[zomato_data['Country Code']==1]

res=zomato_india['City'].value_counts()
city_list=res.index
city_res=res.values
print(city_res)

data=list(zip(zomato_india['City'],zomato_india['Aggregate rating'],zomato_india['Votes']))
weightage_rating=[]
for city in city_list:
    NRate=0
    Tvote=0
    for i in range(len(data)):
        if city in data[i][0]:
            NRate=NRate+(data[i][1]*data[i][2])
            Tvote=Tvote+data[i][2]
    if Tvote!=0:       
        weightage_rating.append(NRate/Tvote) 
    else:
        weightage_rating.append(0)
plt.rcParams["figure.figsize"] = (10,6)
plt.scatter(city_list,city_res,s=weightage_rating,c='red')
plt.xlabel("City").set_color('r')
plt.ylabel("no.of Restaurants").set_color('r')
plt.xticks(rotation=90)
plt.title('cities with Restaurant keeping the weighted restaurant rating of the city in a bubble').set_color('r')
plt.show()

plt.rcParams["figure.figsize"] = (35,8)
plt.scatter(city_list,weightage_rating,s=city_res,c='red',edgecolor='black')
plt.xlabel("City").set_color('r')
plt.ylabel("no.of Restaurants").set_color('r')
plt.xticks(rotation=90)
plt.title('cities with weighted restaurant rating keeping the no.of restaurant in bubble').set_color('r')
plt.show()

plt.rcParams["figure.figsize"] = (20,6)
plt.bar(city_list[0:10],weightage_rating[0:10],color='purple',width=0.5)
plt.xlabel("City").set_color('r')
plt.ylabel("Weighted Restaurant Rating").set_color('r')
plt.title("City vs Weighted Restaurant Rating").set_color('r')
#plt.grid()
plt.xticks(rotation=10,c='black')
plt.show()


# In[ ]:




