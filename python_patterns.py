#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print(i+1,end='')
    print()


# In[7]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


# In[8]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print(i+1,end=' ')
    print()


# In[9]:


n=int(input('enter n value:'))
for i in range(n):
    print((chr(65+i)+' ')*n)


# In[11]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


# In[16]:


n=int(input('enter n value:'))
for i in range(n):
    print((chr(65+i)+' ')*n)


# In[19]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print(j+1,end=' ')
    print()


# In[22]:


n=int(input('enter n value:'))
for i in range(n): #  for evry row i=0,1,2,3,4,..n-1
    for j in range(n): # j=0,1,2,3,4,..n-1
        print(j,end='')
    print()


# In[23]:


n=int(input('enter n value:'))
for i in range(n): #  for evry row i=0,1,2,3,4,..n-1
    for j in range(n): # j=0,1,2,3,4,..n-1
        print(n-j,end='')
    print()


# In[26]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()


# In[28]:


n=int(input('enter n value:'))
for i in range(n):
    print('* ' *(i+1))
      


# In[33]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[35]:


n=int(input('enter n value:'))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[ ]:


print('hello')


# In[ ]:




