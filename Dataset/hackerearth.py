# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:59:50 2020

@author: atul pandey

"""



import numpy as np 
import pandas as pd
import matplotlib.pyplot as plot
import math
from xgboost import XGBClassifier 


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
chhh =test_data.iloc[:,1:]
train_set = train_data.iloc[:,1:]
test_set=   test_data.iloc[:,1:]
breed = train_data.iloc[:,9]
pet = train_data.iloc[:,10]

issue = test_data.iloc[:,1]
issue_train = train_data.iloc[:,1]
listing = test_data.iloc[:,2]



tt = train_set
""""""
testt = test_set
cnt=0
print(cnt)
date=[]
month = []
year=[]
time=[]
for i in listing:
    j = i.split(' ')
    yrs = j[0].split('-')
    tme = j[1].split(':')
    
    date.append(int(yrs[2]))
    month.append(int(yrs[1]))
    year.append(int(yrs[0]))
    time.append(int (tme[0]))

    
        
    


map_color ={}
map_pos={}
color=set()
print((sort_color))
sort_color = sorted(color)
for i in train_set:
    color.add(i[3])
for i in test_set:
    color.add(i[3])
    
cnt =0 

for i in sort_color:
    map_color[i]=cnt
    cnt+=1
cnt =0 
for i in sort_color:
    map_pos[cnt]=i
    cnt+=1
cnt = 0
color_tt = []
for i in range(18834):
    temp =[]
    for j in range(56):
        temp.append(0)
    color_tt.append(temp)

zeros=[]
for i in range(18834):    
    zeros.append(0)
date_str = ["year","month","date","hour"]
for i in test_set:
    color_tt[cnt][map_color[i[3]]]=1
    cnt+=1


  tt.insert(0,"random_varr",new_arr)

for i in range(8072):
    testt['date'][i]
    


tt = tt.drop('random_varr',axis=1)


cnt=0
for  i in chhh['color_type']:
    print(testt[i][cnt])
    testt[i][cnt]=1
    cnt+=1


uu = tt
print(cnt)
arr=[]
cnt=0
sums =0
for i in tt['condition'] :
    if math.isnan(i):
        tt['condition'][cnt] = (sums//(cnt+1))
        cnt+=1
        continue
    sums+=i
    cnt+=1
    
new_arr =[]
for i in range(8072):
    new_arr.append(tt['X1'][i]*tt['height(cm)'][i] + tt['X1'][i]*tt['length(m)'][i]*100 +tt['X2'][i]*tt['height(cm)'][i] + tt['X2'][i]*tt['length(m)'][i]*100 )
        
        
uu = uu.drop(arr,axis=0)
test_set = uu




""" xboost"""

train_model = XGBClassifier()
train_model.fit(tt,breed)

breed_check = train_model.predict(testt)

train_model_pet = XGBClassifier()
train_model_pet.fit(tt,pet)

pet_check = train_model_pet.predict(testt)

cnt=0
for i in breed_check:
    breed_check[cnt] = int(i)
    cnt+=1



pet_id = test_data.iloc[:,0]

final_data = pd.DataFrame({'pet_id':pet_id,'breed_category':breed_check,'pet_category':pet_check})

final_data.to_csv('submission_ran.csv',index=False)