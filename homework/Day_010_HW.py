#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


stock1 = pd.read_csv("STOCK_DAY_0050_202009.csv")
stock2 = pd.read_csv("STOCK_DAY_0050_202010.csv")


# In[14]:


stock1


# In[15]:


stock2


# In[16]:


con_data = pd.concat([stock1,stock2],axis = 0)


# In[17]:


con_data


# In[18]:


con_data[con_data.open < con_data.close]


# In[ ]:




