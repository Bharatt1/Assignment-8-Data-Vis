#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Grade_EdlevelList = zip(names,grades, bsdegrees, msdegrees, phddegrees)
df = pd.DataFrame(data=Grade_EdlevelList,
columns=['Names','Grades', 'BsDegrees', 'MsDegrees', 'PhdDegrees'])
df


# In[17]:


df.sum()


# In[10]:


df.count() # number of values


# In[9]:


df.mean() # arithmetic average


# In[11]:


df.std() # standard deviation


# In[12]:


df.min() # minimum


# In[13]:


df.max() # maximum


# In[14]:


df.quantile(.25) # first quartile


# In[15]:


df.quantile(.5) # second quartile


# In[16]:


df.quantile(.75) # third quartile


# In[20]:


df.median()


# In[21]:


df.mode()


# In[22]:


df.var()

