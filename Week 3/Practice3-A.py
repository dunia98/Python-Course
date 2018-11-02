#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def response(from="USD",to="JOD",amount=1):
print("Avaialabe Currencies: ",available_currencies)


base_curr = input("Choose a currency: ")

response.remove(base_curr)

print("Available to: ", available_currencies)

to_curr = input("Choose from the above: ")

amount = input("How many you want to convert: ")

base_link_forex = 'http://data.fixer.io/api/convert'

parameters_forex = {
    "access_key" : "e1be8ec55a7c5fa9600ff656adf94ac4",
    "from" : base_curr,
    "to" : to_curr,
    "amount" : amount
}

response = requests.get(base_link_forex,parameters_forex).json()

print(response("TRY","USD",50))


# In[ ]:





# In[ ]:




