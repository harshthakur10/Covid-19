#!/usr/bin/env python
# coding: utf-8

# ## Create a Python script to fetch the latest COVID-19 data for Indian states from the provided API URL: https://data.covid19india.org/v4/min/timeseries.min.json. The script should print the response of the JSON data.
# 

# In[3]:


import requests 

url="https://data.covid19india.org/v4/min/timeseries.min.json"


# In[4]:


r=requests.get(url)


# In[5]:


r


# In[6]:


r.content


# In[ ]:




