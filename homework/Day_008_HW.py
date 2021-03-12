#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[6]:


name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']

sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']

weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]

rank_list = [8,1,5,4,7,6,2,3]

myopia_list = [True,True,False,False,True,True,False,False]


# In[7]:


dt = np.dtype({'names' : ('name', 'sex', 'weight', 'rank', 'myopia'), 'formats' : ((np.str_, 5), (np.str_, 5), np.float, int, bool)})


# In[8]:


array1 = np.zeros(8, dtype = dt)
array1


# In[9]:


array1['name'] = name_list
array1['sex'] = sex_list
array1['weight'] = weight_list
array1['rank'] = rank_list
array1['myopia'] = myopia_list


# In[10]:


array1


# In[11]:


print("average weight = ", np.mean(array1['weight']))


# In[12]:


print("Boys' average weight = ", np.mean(array1[array1['sex'] == 'boy']['weight']))


# In[13]:


print("Girls' average weight = ", np.mean(array1[array1['sex'] == 'girl']['weight']))

