#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=' ')
    print()


# In[3]:


# diamond pattern


# In[4]:


n=int(input('enter n value:'))
for i in range(n):
    print(' '*(n-i-1),end='')
    print('*  '*(i+1))
    print()


# In[ ]:




