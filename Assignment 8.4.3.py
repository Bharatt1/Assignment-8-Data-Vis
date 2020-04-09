#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv(r"C:\Users\\Brian\Python\Previous_Assignments\gradedata.csv")
plt.scatter(df.hours, df.grade)

# There is a positive linear relationship between the hours a student puts in and the grade they receive. 

