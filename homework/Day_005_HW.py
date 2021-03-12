#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])


# In[11]:


# 平均
mean_eng = np.mean(english_score)
mean_math = np.nanmean(math_score)
mean_ch = np.mean(chinese_score)

# 最大值
max_eng = np.max(english_score)
max_math = np.nanmax(math_score)
max_ch = np.max(chinese_score)

#最小值
min_eng = np.min(english_score)
min_math = np.nanmin(math_score)
min_ch = np.min(chinese_score)

#標準差
std_eng = np.std(english_score)
std_math = np.nanstd(math_score)
std_ch = np.std(chinese_score)

print("英文平均 : {} 分, 數學平均 : {} 分, 國文平均 : {} 分".format(mean_eng, mean_math, mean_ch))
print("英文最高分 : {} 分, 數學最高分 : {} 分, 國文最高分 : {} 分".format(max_eng, max_math, max_ch))
print("英文最低分 : {} 分, 數學最低分 : {} 分, 國文最低分 : {} 分".format(min_eng, min_math, min_ch))
print("英文標準差 : {} , 數學標準差 : {} , 國文標準差 : {} ".format(std_eng, std_math, std_ch))


# In[12]:


# 補考後成績
math_score[4] = 55
print(math_score)


# In[13]:


# 平均
mean_eng = np.mean(english_score)
mean_math = np.nanmean(math_score)
mean_ch = np.mean(chinese_score)

# 最大值
max_eng = np.max(english_score)
max_math = np.nanmax(math_score)
max_ch = np.max(chinese_score)

#最小值
min_eng = np.min(english_score)
min_math = np.nanmin(math_score)
min_ch = np.min(chinese_score)

#標準差
std_eng = np.std(english_score)
std_math = np.nanstd(math_score)
std_ch = np.std(chinese_score)

print("英文平均 : {} 分, 數學平均 : {} 分, 國文平均 : {} 分".format(mean_eng, mean_math, mean_ch))
print("英文最高分 : {} 分, 數學最高分 : {} 分, 國文最高分 : {} 分".format(max_eng, max_math, max_ch))
print("英文最低分 : {} 分, 數學最低分 : {} 分, 國文最低分 : {} 分".format(min_eng, min_math, min_ch))
print("英文標準差 : {} , 數學標準差 : {} , 國文標準差 : {} ".format(std_eng, std_math, std_ch))


# In[18]:


en_ch = np.corrcoef([english_score, chinese_score])
ma_ch = np.corrcoef([math_score, chinese_score])


# In[19]:


print(en_ch)


# In[22]:


if  (en_ch[0, 1] > ma_ch[0, 1]):
    print("英文的相關係數較大")
else: 
    print("數學的相關係數較大")


# In[ ]:




