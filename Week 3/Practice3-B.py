#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests

link = "http://api.openweathermap.org/data/2.5/weather"


additional_data = {
    "APPID" : "7bd564fc6c9bbb43d62c03c2585a9c91",
    "q": "Amman,Jo",
    "units" : "metric"
}

data = requests.get(link,params=additional_data).json()

print(data)


# In[ ]:




