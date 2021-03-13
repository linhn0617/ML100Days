#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


answer = pd.read_csv('boston.csv',usecols = ['CHAS','NOX','RM'])


# In[10]:


answer


# In[12]:


answer_xlsx = answer.to_excel('answer.xlsx')


# In[13]:


result = pd.read_excel('answer.xlsx',usecols = ['CHAS','NOX','RM'])


# In[14]:


result

