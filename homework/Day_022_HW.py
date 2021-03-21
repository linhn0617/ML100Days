#!/usr/bin/env python
# coding: utf-8

# In[21]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
#決定底框
plt.axes([0.1,0.1,.5,.5])
#給定刻度, 若不給定值, 圖的周邊無文字
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)

'''
#決定第二層框


#決定第三層框


#決定第四層框

'''


# In[22]:


#決定底框
plt.axes([0.1,0.1,.5,.5])
plt.xticks([]), plt.yticks([])
plt.text(0.1,0.1, 'axes([0.1,0.1,.5,.5])',ha='left',va='center',size=16,alpha=.5)
#決定第二層框
plt.axes([0.3,0.3,.5,.5])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.3,0.3,.5,.5])',ha='left',va='center',size=16,alpha=.5)
#決定第三層框
plt.axes([0.5,0.5,.5,.5])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.5,0.5,.5,.5])',ha='left',va='center',size=16,alpha=.5)

#決定第四層框
plt.axes([0.7,0.7,.5,.5])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,'axes([0.7,0.7,.5,.5])',ha='left',va='center',size=16,alpha=.5)


# In[57]:


#配置12 組 Bar
n = 12 
X = np.arange(n)

 #給定數學運算式
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

#指定繪製區域, 給定 Bar 顏色, 邊界顏色
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor = 'red', edgecolor = 'white')
# +Y 指的是 XY 四象限的第一象限
# -Y 指的是 XY 四象限的第二象限

 #設定繪圖圖示區間
for x,y in zip(X,Y1):
    plt.text(x, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
for x,y in zip(X,Y2):
    plt.text(x, -(y+0.05), '%.2f' % y, ha='center', va= 'top')
 #設定Y軸區間
plt.ylim(-1.25,+1.25)

