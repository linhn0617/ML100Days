#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


import os
os.getcwd()

df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")


# In[3]:


#資料整理
df_red["color"] = "R"
df_white["color"] = "W"

#整合紅酒與白酒的資料
df_all=pd.concat([df_red,df_white],axis=0)

# 檢查合併後的資料集
df_all.head()


# In[4]:


df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)
# 檢查合併後的資料集
df_all.head()


# In[5]:


sns.histplot(df_all["quality"])


# In[12]:


#建立一個Figure（空的顯示區）
fig = plt.figure()

#直接製圖在剛剛建立的figure
ax1 = plt.subplot(221)
ax2 = plt.subplot(223)
ax3 = plt.subplot(122)

#避免多個圖重疊，使用tight_layout分開, 可以節省新增Figure的軸的動作
plt.tight_layout()


# In[13]:


df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False) 
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[14]:


#作業一：更改bin的值
df_all.hist(bins=5, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=False) 
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[15]:


#作業二：更改grid
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True) 
plt.tight_layout(rect=(0, 0, 1.2, 1.2))


# In[17]:


#作業三：更改 plt.tight_layout(rect=(x1, y1, x2, y2)), x / y 值
df_all.hist(bins=10, color='lightblue',edgecolor='blue',linewidth=1.0,
          xlabelsize=8, ylabelsize=8, grid=True) 
plt.tight_layout(rect=(1, 1, 2, 2))


# In[ ]:




