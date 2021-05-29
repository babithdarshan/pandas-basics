#!/usr/bin/env python
# coding: utf-8

# In[10]:


for i in range(10):
    if i==7:
        print('loop excution is enough plz break the loop')
    print(i)
       


# In[11]:


cart=[10,20,600,60,70]
for item in cart:
    if item >500:
        print('to place this order insurance must be required')
        break
    print(item)


# In[13]:


for i in range(10):
    if i==8:
        continue
    print(i)
        


# In[42]:


cart=[10,20,500,600,700]
for item in cart:
    if item >= 500:
        
        
        print('we cannot process this item because of insurance issue:',item)
        continue
    print('processing item:',item)


# In[53]:


numbers =[10,20,0,5,0,30]
for n in numbers:
    if n == 0:
         continue
    print('100/{}= {}'.format(n,100/n))


# In[78]:


n=int(input('enter your size:'))
size=[28,30,32,34]
for n in size:
    if n <28:
        print('this size is avaliable')
    elif n>28:
        
        ('print size is out of stock')
    else:
        print('have a good shopping')


# In[85]:


cart=[10,20,700,800,900]
for item in cart:
    if item >500:
        print('we cannot process the item')
        break
    print('processing the item:',item)


# In[ ]:




