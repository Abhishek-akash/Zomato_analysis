#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import os
import matplotlib.pyplot as plt
#print(pwd)
file=pd.read_csv(r"C:\Users\Dell\Desktop\zomato.csv",encoding='ISO-8859–1')
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
print("Total cuisines in  Delhi-NCR-->",len(set(all_delhi_cuisine)))
l2_cuisines=[]
all_RestIndia_cuisine=[]
for i in RestIndia_cuisines:
    sep_list=i.split(',')
    if len(sep_list)>1:
        for j in sep_list:
            all_RestIndia_cuisine.append(j.strip())
    else:
        all_RestIndia_cuisine.append(sep_list[0].strip())
print("Total cussines in rest of india-->",len(set(all_RestIndia_cuisine)))
print("-----------------------------------------")
print("*** The cuisines which are not present in restaurant of Delhi NCR but present in rest of India ***")
print("----------------------------------------------------------------------------------------------")
for i in set(all_RestIndia_cuisine)-set(all_delhi_cuisine):
    print("     ->",i)

print("----------------------------------------------------------------------------------------------")
print("CUISINES THAT ARE NOT SERVED IN DELHI_NCR USING ZOMATO API:")
print("----------------------------------------------------------------------------------------------")
print("    ->German")
print("    ->Cajun")


# In[ ]:




