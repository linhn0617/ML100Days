#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np


# In[12]:


x = np.arange(0,180)
y = np.cos(x)


# In[16]:


x


# In[17]:


y


# In[18]:


plt.plot(x,y)
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.title("The Title") 
plt.show() 


# In[21]:


plt.scatter(x,y)
plt.title("Scatter plot")


# In[26]:


plt.plot(x,x,'c-.')


# In[ ]:




