#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


array1 = np.array(range(30))
array2 = np.array([2,3,5])


# In[11]:


with open ('two_array.npz','wb') as f:
    np.savez(f,array1,array2)
npzfile = np.load('two_array.npz')
type(npzfile)


# In[12]:


npzfile.files


# In[13]:


print(npzfile['arr_0'])
print(npzfile['arr_1'])


# In[16]:


array3 = np.array([[4,5,6],[1,2,3]])
np.savez('three_array.npz',npzfile['arr_0'],npzfile['arr_1'],array3)


# In[19]:


answer = np.load('three_array.npz')
answer.files


# In[21]:


answer['arr_0']


# In[22]:


answer['arr_1']


# In[23]:


answer['arr_2']


# In[ ]:




