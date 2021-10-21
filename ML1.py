#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
print(a)


# In[2]:


s1="Deepti"
print(s1)


# In[3]:


a=10
b=1
print(a+b)


# In[4]:


a=1
b=2
a=a+b
b=a-b
a=a-b
print(a,b)


# In[52]:


a=10
b=20
if(b>a):
    print(b,"is greater than",a)
else:
    print(a,"is greater than ",b)


# In[11]:


for i in range(3):
    print(i)


# In[19]:


def calc(a,b,c):
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    elif c=="/":
        if b>0:
            print(a/b)
        else:
            print("Cannot divide by zero")
    else:
        print("invalid operator")
a=int(input("Enter value for a"))
b=int(input("Enter value for b"))
c=input("enter a character")
calc(a,b,c)
        


# In[22]:


a=[2,"abc"]
for i in a:
    print(i,"\n")


# In[55]:


a="hi"
b="hello"
print(bool(a<b))


# In[42]:


c=b[::-1]
print(c)


# In[60]:


l1=[10,20,30,40,50]
l2=["hi","hello"]
l2[0]="abc"
print(l1+l2)

for i in l1:
    print(i)
l1.append(20)
for i in l1:
    print(i)


# In[87]:


d={'Name':"Deepti",'USN':"051"}
d['Age']=21
print(len(d))
print("Name:",d["Name"])
for key,value in d.items():
    print(key,value)
for v in d.values():
    print(v)


# In[75]:


t=(10,20,30,40,50)
t[0]=11
print(t[0])


# In[ ]:





# In[ ]:




