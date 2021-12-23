#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import random
from sklearn.preprocessing import StandardScaler

col_names=['x1','x2','res']
ds=pd.read_csv('Student-University.csv',header=None,names=col_names)
scaler=StandardScaler()
scaler.fit(ds)
test=ds.values.tolist()

train=[]
for i in range(80):
    r=random.randrange(len(test))
    train.append(test.pop(r))
  
print(len(train),len(test))

print(train)


# In[59]:


import numpy as np
b0=0.0
b1=0.0
b2=0.0
alpha=0.001

x1=[i[0] for i in train]
x2=[i[1] for i in train]
y_train=[i[2] for i in train]


epoch=10000

while(epoch>0):
    for i in range(len(train)):
        pred=1/(1+np.exp(-(b0+b1*x1[i]+b2*x2[i])))
        print(np.ceil(pred),y_train[i])
        b0=b0+alpha*(y_train[i]-pred)*pred*(1-pred)*1.0
        b1=b1+alpha*(y_train[i]-pred)*pred*(1-pred)*x1[i]
        b2=b2+alpha*(y_train[i]-pred)*pred*(1-pred)*x2[i]
    epoch=epoch-1
    




# In[60]:


b0,b1,b2


# In[61]:


x3=[i[0] for i in test]
x4=[i[1] for i in test]
y_test=[i[2] for i in test]
pred=[]
for i in range(len(test)): 
    pred1=1/(1+np.exp(-(b0+b1*x3[i]+b2*x4[i])))
    pred1=np.ceil(pred1)
    pred.append(pred1)
    print(pred1,y_test[i])
    


# In[62]:


from sklearn.metrics import accuracy_score

accuracy_score(y_test,pred)


# In[ ]:




