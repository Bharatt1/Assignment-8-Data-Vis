#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(r"C:\Users\\Brian\Python\Previous_Assignments\gradedata.csv")
df.head()


# In[6]:


df.max()


# In[7]:


df.hist(column="age", by="gender")

