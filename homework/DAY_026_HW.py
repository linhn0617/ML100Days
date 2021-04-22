#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import IFrame

IFrame('https://demo.bokeh.org/sliders', width=900, height=500)


# In[2]:


from bokeh.plotting import figure, output_file, show

output_file("tool.html") #輸出的名稱

# create a new plot with the toolbar below

p = figure(plot_width=400, plot_height=400,

          title="tool", toolbar_location="below",

          toolbar_sticky=False)

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)


# In[4]:


import bokeh.io
from bokeh.resources import INLINE
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd

# 環境 settings
bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)


# In[11]:


#第一題

#指定輸出檔名
output_file("DAY_026-1.html")

#給定資料
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

# 不增設按鈕 toolbar_location=None, tools=""
# plot_height 設定條形高度
#配置圖表
hw1 = figure(x_range=fruits, title="Fruit Counts",
           toolbar_location=None, tools="")

hw1.vbar(x = fruits,top = counts,width = 0.5)

#Y座標從0開始
hw1.y_range.start = 0

show(hw1)


# In[13]:


#第二題
output_file("DAT_026-2.html")

#給定資料
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]
#資料做排序
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])
counts.sort()
# 不增設按鈕 toolbar_location=None, tools=""
# plot_height 設定條形高度
# 配置圖表
hw2 = figure(x_range=sorted_fruits, title="Sorted_Fruit Counts",
           toolbar_location=None, tools="")

hw2.vbar(x=sorted_fruits, top = counts, width = 0.5)

# Y座標從0開始
hw2.y_range.start = 0

show(hw2)

