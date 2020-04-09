#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\\Brian\Python\Previous_Assignments\gradedata.csv")
df.tail()


# In[3]:


df.take(np.random.permutation(len(df))[:500])

