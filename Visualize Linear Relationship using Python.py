#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install plotly.express


# In[4]:


pip install matplotlib.pyplot


# In[5]:


pip install seaborn 


# In[6]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding = 'latin1')
data = data.dropna()
print(data.head())


# In[ ]:




