#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)


# In[4]:


week_series=series.resample('W',convention='start').asfreq()
week_series


# In[5]:


week_series.mean()


# In[ ]:




