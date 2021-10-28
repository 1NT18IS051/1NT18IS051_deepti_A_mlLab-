#!/usr/bin/env python
# coding: utf-8

# In[62]:


import math
l=[1,2,3,4,1,2,3,3]
n=len(l)
sum=0

#mean
for i in l:
    sum=sum+i
mean=sum/n
print("Mean is",mean)

#mode
fr=[0]*max(l)
for ele in l:
    fr[ele-1]+=1
m=fr.index(max(fr))+1

    
print("Mode is",m)
   
#S.D and variance
sum=0
for i in l:
     sum+=pow((i-mean),2)
print("Variance is",sum/(n-1))
print("S.D is",math.sqrt(sum/(n-1)))

#median
l.sort()

if(n%2==1):
    k=math.floor(n/2)
    print("Median is",l[k])
else:
    m=int(n/2)
    a=l[m]+l[m-1]
    print("Median is",a/2)



# In[58]:


import statistics as st
l1=[1,2,3,4,1,2,3,3]
print(st.mean(l1))
print(st.mode(l1))
print(st.variance(l1))
print(st.stdev(l1))
print(st.median(l1))


# In[ ]:





# In[ ]:




