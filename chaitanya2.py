#!/usr/bin/env python
# coding: utf-8

# In[10]:


for i in range(0,5):
    print(i)
    for j in range(0,5):
        print("*")
    


# In[18]:


for i in range(0,5):
    for j in range(0,i+1):
        print("*",end="")
    print('')


# In[20]:


a=1
while(a<10):
    if(a==6):
        break
    print(a)
    a=a+1


# In[ ]:


a=1
while(a<10):
    if(a==6):
        continue
    print(a)
    a=a+1


# In[ ]:




