# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:31:46 2020

@author: Atul Pandey
"""






import numpy as np

import matplotlib.pyplot as plot 
import pandas as pd
from xgboost import XGBClassifier
dataset = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
x_set = dataset.iloc[:,5:-2]
breed = dataset.iloc[:,9]
pet = dataset.iloc[:,10]

"""
from sklearn.preprocessing import LabelEncoder , OneHotEncoder 
labelencode_x = LabelEncoder()
x_set[:,3] = labelencode_x.fit_transform(x_set[:,3])
onehotencoder = OneHotEncoder(categorical_features =[3])
x_set = onehotencoder.fit_transform(x_set).toarray()
"""

test_data  = test.iloc[:,5:]

"""
from sklearn.model_selection import   train_test_split
x_train , x_test,y_train,y_test = train_test_split(x_set,y_set,test_size=0.2 , random_state = 0)
"""
from sklearn.linear_model import LinearRegression 
regressor_pet = LinearRegression()
regressor_pet.fit(x_set,pet)
regressor_breed = LinearRegression()
regressor_breed.fit(x_set,breed)




breed_pred= regressor_breed.predict(test_data)
breed_data = []
cnt = 0 

for i in breed_pred :
    p = i - int(i)
    temp = int(i)
    if(p>0.5):
        temp+=1
    breed_data.append(temp)
        


pet_pred= regressor_pet.predict(test_data)
pet_data = []
cnt = 0 

for i in pet_pred :
    
    pet_data.append( int(round(i )) )
    

pet_id = test.iloc[:,0]

final_data = pd.DataFrame({'pet_id':pet_id,'breed_category':breed_data,'pet_category':pet_data})

final_data.to_csv('submission2.csv',index=False)
    


