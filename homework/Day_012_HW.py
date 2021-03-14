#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np


# In[16]:


bos = pd.read_csv('boston.csv')
bos


# In[17]:


bos.boxplot()


# In[19]:


for name in bos.columns:
    if(400 > np.median(bos[name]) > 300):
        print(name)


# In[20]:


bos.plot.scatter(x = "NOX", y = "DIS")


# #兩者為反比關係
