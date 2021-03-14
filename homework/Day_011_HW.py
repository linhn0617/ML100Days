#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


q_df = pd.DataFrame([['male', 'teacher'], 
              ['male', 'engineer'],
              ['female', None],
              ['female', 'engineer']],columns=['Sex','Profession'])
q_df


# In[3]:


q_df.fillna('others')


# In[ ]:


#用一般性資料編碼比較適合,職業並沒有順序之分

