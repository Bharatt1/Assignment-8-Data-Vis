#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\\Brian\Python\Previous_Assignments\gradedata.csv")
df.head()


# In[2]:


df = df.sort_values(by=['fname', 'age', 'grade'],
ascending=[True, True, True])
df.head()

