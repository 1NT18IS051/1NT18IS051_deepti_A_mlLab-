#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('C:/Users/Computer/Downloads/pima.csv')
data.head()


# In[13]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
from matplotlib import rcParams
import pandas_profiling


# In[14]:


warnings.filterwarnings("ignore")
rcParams["figure.figsize"]=10,6
np.random.seed(42)
data.sample(5)


# In[15]:


data.columns


# In[16]:


X=data.drop("Outcome",axis=1)
y=data["Outcome"]


# In[17]:


scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)


# In[18]:


X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,y,stratify=y,test_size=0.10,random_state=42)


# In[19]:


classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train,Y_train)


# In[20]:


y_pred = classifier.predict(X_test)


# In[21]:


print("Accuracy:",accuracy_score(Y_test,y_pred))


# In[22]:


feature_importances_df = pd.DataFrame(
    {"feature":list(X.columns),"importance":classifier.feature_importances_}
).sort_values("importance",ascending=False)

feature_importances_df


# In[23]:


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(X_train,Y_train)


# In[24]:


Y_pred = clf.predict(X_test)


# In[25]:


from sklearn.metrics import accuracy_score
print("Accuracy-DecisionTree :",accuracy_score(Y_test,Y_pred))


# In[ ]:




