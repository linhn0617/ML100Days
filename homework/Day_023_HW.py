#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# 載入數據集
tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")


# In[4]:


tips.head()


# In[5]:


# 作業一
sns.relplot(x="total_bill", y="tip", hue="sex", style="time", data=tips);


# In[9]:


fmri.head()


# In[13]:


sns.relplot(x="timepoint", y="signal", hue="event", style="region", data=fmri);


# In[14]:


sns.regplot(x="timepoint", y="signal", data=fmri);


# In[ ]:




