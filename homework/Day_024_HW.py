#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 導入必要的程式庫
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
df = sns.load_dataset('titanic')


# In[2]:


df.info()


# In[4]:


# 直接使用PANDAS dataframe, 當作參數
# 條形圖()顯示分類變數和連續變數之間的關係。數據以矩形條表示,其中條的長度表示該類別中數據的比例。
# x, y 表示特徵值, data 給定dataframe 
ax = sns.barplot(x="sex", y="survived", data=df,hue = 'class')


# In[5]:


df = sns.load_dataset('tips')


# In[6]:


df.info()


# In[10]:


sns.boxplot(x='time', y='tip', data=df)
sns.stripplot(x='time', y='tip', data=df, jitter=True)
plt.show()

