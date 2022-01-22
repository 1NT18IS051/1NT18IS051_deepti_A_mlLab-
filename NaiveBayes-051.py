#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
df = pd.read_csv('C:/Users/Computer/Downloads/covid.csv')
df.head()


# In[3]:


from sklearn import preprocessing
le = preprocessing.LabelEncoder()
pc_encoded=le.fit_transform(df['pc'].values)
wbc_encoded=le.fit_transform(df['wbc'].values)
mc_encoded=le.fit_transform(df['mc'].values)
ast_encoded=le.fit_transform(df['ast'].values)
bc_encoded=le.fit_transform(df['bc'].values)
ldh_encoded=le.fit_transform(df['ldh'].values)
Y=le.fit_transform(df['diagnosis'].values)


# In[4]:


X=np.array(list(zip(pc_encoded,wbc_encoded,mc_encoded,ast_encoded,bc_encoded,ldh_encoded)))
print(X)
print(Y)


# In[5]:


from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
model = MultinomialNB()


# In[6]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y)


# In[7]:


model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
print("Accuracy:",accuracy_score(Y_test, y_pred))
print("\nReport")
print(classification_report(Y_test,y_pred))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




