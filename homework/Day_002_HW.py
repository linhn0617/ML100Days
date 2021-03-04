#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
array1 = np.array(range(30))
result = array1.reshape(5,6,order="F")
print(result)


# In[5]:


import numpy as np
array1 = np.array(range(30))
result = array1.reshape(5,6,order="F")
result1 = np.where(result%6==1)
print(result1)


# In[ ]:




