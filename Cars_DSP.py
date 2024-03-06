#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\abir1\Music\cars.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.isnull().sum()


# In[10]:


data.isnull().sum()


# In[18]:


make_count=data["Make"].value_counts()


# In[19]:


make_count


# In[20]:


filter_record=data[data["Origin"].isin(["Asia","Europe"])]


# In[21]:


filter_record


# In[22]:


d_weight=data[data["Weight"]<=4000]


# In[23]:


d_weight


# In[24]:


data["MPG_City"]+=3


# In[25]:


data["MPG_City"]


# In[27]:


data.isnull().sum()


# In[29]:


data["Cylinders"].fillna(data["Cylinders"].mean(), inplace=True)


# In[31]:


data["Length"].fillna(data["Length"].mean(), inplace=True)


# In[33]:


data["Weight"].fillna(data["Weight"].mean(), inplace=True)


# In[ ]:




