#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\\Brian\Python\Previous_Assignments\gradedata.csv")
df.head()


# In[6]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ age + exercise + hours',
data=df).fit()
result.summary()


# In[7]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours',
data=df).fit()
result.summary()


# In[8]:


df.gender[df.gender == 'male'] = 0
df.gender[df.gender == 'female'] = 1
print(df)


# In[10]:


import statsmodels.formula.api as sm
result = sm.ols(
formula='grade ~ exercise + hours + gender',
data=df).fit()
result.summary()
# the addition of gender as a varaible does not affect the model as the adjusted r-squared, which is used to compare between models is the same. In addition, the p-value for gender is above .05.

