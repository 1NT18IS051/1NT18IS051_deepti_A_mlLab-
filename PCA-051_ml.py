#!/usr/bin/env python
# coding: utf-8

# In[15]:




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
X = pd.read_csv(r'C:\Users\Computer\Downloads\Iris.csv')
X.head()









# In[16]:


df.describe()


# In[17]:



species =df.species
species=species.tolist()


# In[18]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X=scaler.fit_transform(X)


# In[19]:


X_corr = (1 / 150) * X.T.dot(X)


# In[20]:


u,s,v = np.linalg.svd(X_corr)
eig_values, eig_vectors = s, u
eig_values, eig_vectors


# In[21]:


np.linalg.eig(X_corr)


# In[24]:


total = sum(eig_values)
variance_of_each_feature =(eig_values / np.sum(eig_values))*100
print("variance of each feature-->",variance_of_each_feature)
plt.figure(figsize=(8,4))
plt.bar(range(5),variance_of_each_feature, alpha=0.6)
plt.ylabel('Percentage of explained variance')
plt.xlabel('Dimensions')


# In[25]:


pc1 = X.dot(eig_vectors[:,0])
pc2 = X.dot(eig_vectors[:,1])


# In[26]:


# plotting in 2D
def plot_scatter(pc1, pc2):
    fig, ax = plt.subplots(figsize=(15, 8))
    
    species_unique = list(set(species))
    species_colors = ["r","b","g"]
    
    for i, spec in enumerate(species):
        plt.scatter(pc1[i], pc2[i], label = spec, s = 20, c=species_colors[species_unique.index(spec)])
        ax.annotate(str(i+1), (pc1[i],pc2[i]))
    
    from collections import OrderedDict
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), prop={'size': 15}, loc=4)
    
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.axhline(y=0, color="grey", linestyle="--")
    ax.axvline(x=0, color="grey", linestyle="--")
    
    plt.grid()
    plt.axis([-4, 4, -3, 3])
    plt.show()
    
plot_scatter(pc1, pc2)


# In[ ]:




