#!/usr/bin/env python
# coding: utf-8

# In[3]:


def print_prime_numbers(n):
    
    n=int(input("enter number and check if it is a prime number or not :"))
    for i in range(1,n):
        i=i+1
        if i%n==0:
            print(f"{n} is a composite number")
            break
        else:
            print(f"{i} is a prime number")
        
    
print_prime_numbers(20)    


# In[ ]:




