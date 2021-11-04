#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy
x=0
M=0
sum=0
l=[20,10,30,44,55]
x=numpy.min(l)
M=numpy.max(l)

for i in range(0,len(l)):
    l[i]=(l[i]-x)/(M-x)
    sum+=l[i]
print(sum/len(l))


# In[73]:


from sklearn.preprocessing import Normalizer
X=[[0, 6,5], [0, 9,7], [1, 1,9]]
#T=Normalizer().fit(X)

#T.transform(X)
print(Normalizer().transform(X).mean())
print(Normalizer().transform(X).std()) #=0
print(Normalizer().fit_transform(X))


# In[66]:


from sklearn.preprocessing import StandardScaler
p=[[0, 0], [0, 0], [1, 1], [1, 1]]

print(StandardScaler().fit_transform(p).mean())
print(StandardScaler().fit_transform(p))
print(StandardScaler().fit_transform(p).std()) #=1


# In[60]:


import statistics as std
l=[12,34,56,11,2,8]
s=std.stdev(l)
m=std.mean(l)
for i in range(0,len(l)):
    l[i]=(l[i]-m)/s
print(std.mean(l))
print(std.stdev(l))


# In[ ]:




