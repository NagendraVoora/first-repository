# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:01:21 2022

@author: DEEPTHI
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
data=pd.read_csv("salaries.csv")
print(data)
x=data.drop(['salary_more_then_100k'],axis=1)
y=data['salary_more_then_100k']
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()
x['company_n']=le_company.fit_transform(x['company'])
x['job_n']=le_company.fit_transform(x['job'])
x['degree_n']=le_company.fit_transform(x['degree'])
x=x.drop(columns=['company','job','degree'],axis=1)
model=tree.DecisionTreeClassifier()
model.fit(x,y)
model.score(x,y)
num=np.array(([0,2,2],[2,0,0]),dtype=int)
model.predict(num)
