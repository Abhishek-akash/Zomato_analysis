#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os
import collections
import matplotlib.pyplot as plt
#print(pwd)
file=pd.read_csv(r'/Users/abhishek.kumar13027/Downloads/zomato.csv')
df=file.copy()
df=df[df['Country Code']==1]
af=df[df['Country Code']==1]
IndianCity_count=af.City.value_counts().sum()
#print("total restaurant in indian cities-->",IndianCity_count)
af=af[(af['City'] != 'New Delhi')&(af['City'] != 'Ghaziabad')&(af['City'] != 'Noida')&(af['City'] != 'Gurgaon')&(af['City'] != 'Faridabad')]
df=df[(df['City']=='New Delhi')|(df['City']=='Ghaziabad')|(df['City']=='Noida')|(df['City']=='Gurgaon')|(df['City']=='Faridabad')]
DelhiNCR_cuisines=df.Cuisines.value_counts().index
RestIndia_cuisines=af.Cuisines.value_counts().index
#print("total cuisines in Delhi-Ncr Delhi-NCR-->",len(DelhiNCR_cuisines))
#print("Total cussines in rest of india-->",len(RestIndia_cuisines))
l1_cuisines=[]
all_delhi_cuisine=[]
for i in DelhiNCR_cuisines:
    sep_list=i.split(',')
    if len(sep_list)>1:
        for j in sep_list:
            all_delhi_cuisine.append(j.strip())
    else:
        all_delhi_cuisine.append(sep_list[0].strip())
#print("Total cuisines in  Delhi-NCR-->",len(set(all_delhi_cuisine)))
l2_cuisines=[]
all_RestIndia_cuisine=[]
for i in RestIndia_cuisines:
    sep_list=i.split(',')
    if len(sep_list)>1:
        for j in sep_list:
            all_RestIndia_cuisine.append(j.strip())
    else:
        all_RestIndia_cuisine.append(sep_list[0].strip())
#print("Total cussines in rest of india-->",len(set(all_RestIndia_cuisine)))
Delhi_Ncr_dict={}
Rest_India_dict={}
for i in set(all_delhi_cuisine):
    Delhi_Ncr_dict[i]=all_delhi_cuisine.count(i)
for i in set(all_RestIndia_cuisine):
    Rest_India_dict[i]=all_RestIndia_cuisine.count(i)
DelhiNCR_sorted_dict=collections.OrderedDict(sorted(Delhi_Ncr_dict.items(),key=lambda x:x[1],reverse=True)) 
RestIndia_sorted_dict=collections.OrderedDict(sorted(Rest_India_dict.items(),key=lambda x:x[1],reverse=True)) 
print("-----------------------********************************--------------------------------------")
print("Top 10 cuisines served by most restaurant of Delhi NCR") 
print("----------------------------------------------------------------------------------------------")
count=0 
for key,value in DelhiNCR_sorted_dict.items(): 
    if count<10: 
        print(key,"-->",value)
        count+=1 
    else:
        break
print("-----------------------********************************--------------------------------------")
print("*** Top 10 cuisines served by most restaurant of Rest India ***")
print("----------------------------------------------------------------------------------------------")
count=0 
for key,value in RestIndia_sorted_dict.items(): 
    if count<10: 
        print(key,"-->",value)
        count+=1 
    else:
        break



    

