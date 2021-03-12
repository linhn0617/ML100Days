#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array1 = np.array([[10, 8], [3, 5]])


# In[5]:


inv_array = np.linalg.inv(array1)
inv_array


# In[6]:


ans = inv_array @ array1

if ans.all() == np.identity(2).all():
    print("是單位矩陣")
else:
    print("不是單位矩陣") #question1


# In[7]:


a, b = np.linalg.eig(array1)

print("eigenvalues = {}\neigenvectors = \n{}".format(a, b))


# In[8]:


u, s, vh = np.linalg.svd(array1)
print("SVD: \n u = \n{}\ns = {}\n vh = \n{}".format(u, s, vh))


# In[ ]:




