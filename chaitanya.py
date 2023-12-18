#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=20
print(a+b)


# In[6]:


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
    
    
    
    


# In[7]:


a=int(input("enter a number:"))
if a%2==0:
    print("The number is even")
else:
    print("then number is odd")


# In[16]:


Amount=int(input("Enter the total amount"))
if Amount>2500:
    print("You have discount of 10%:")
    Discount_prize=Amount*10/100
    print("Discounted Amount",Discount_prize)
    print("Discount prize:",Amount-Discount_prize)
else:
    print("You don't have discount")


# In[21]:


a=int(input("Enter a number:"))
if a>0:
    print("a is postive number")
elif a==0:
    print("a is neither postive nor negative")
else:
    print("a is negative number")


# In[27]:


a=int(input("Enter First number"))
b=int(input("Enter Second number"))
o=input("Enter a operator:+,-,*,%")
if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
elif o=="*":
    print(a*b)
elif o=="/":
    print(a/b)
elif o=="%":
    print(a%b)
else:
    print("invalid option")
    


# In[29]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b & a>c:
    print("a is greater number")
elif b>c & b>a:
    print("b is greater number")
else:
    print("c is greater number")


# In[34]:


import random
num=random.random()
num


# In[36]:


a=[100,200,160]
x=random.choice(a)
x


# In[42]:


a=["stone","paper","scissor"]
system=random.choice(a)
user=input("select stone or paper or scissor")
print(system)
print(user)
if system==user:
    print("draw")
elif system=="stone" and user=="scissor":
    print("system win")
elif system=="paper" and user=="scissor":
    print("user win")
elif system=="stone" and user=="paper":
    print("user win")
elif system=="scissor" and user=="paper":
    print("system win")
elif system=="paper" and user=="stone":
    print("system win")
elif system=="scissor" and user=="stone":
    print("user win")


# In[49]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b:
    if a>c:
        print("a is greater number")
    else:
        print("c is greater number")
elif c>b:
    print("c is greater number")
else:
    print("b is greater number")
    


# In[ ]:




