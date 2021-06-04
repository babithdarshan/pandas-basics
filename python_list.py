#!/usr/bin/env python
# coding: utf-8

# In[3]:


l=eval(input('enter list:'))


# In[4]:


type(l)


# In[7]:


l=list(range(10))


# In[8]:


print(l)


# In[10]:


l=list({10,20,30,40,50})


# In[11]:


print(l)


# In[12]:


type(l)


# In[13]:


s='learning python is very easy'
l=s.split()
print(l)


# In[14]:


l=[10,20,30,40]


# In[17]:


print(l[-1])


# In[20]:


print(l[0])


# In[21]:


print(l[1])


# In[22]:


print(l[2])


# In[23]:


print(l[3])


# In[29]:


l=list('abcdefghij')


# In[31]:


print(l)


# In[32]:


print(l[2:7:2])


# In[36]:


l[4:2:-2]


# In[37]:


l[8:2:-2]


# In[38]:


print(l[4::2])


# In[39]:


print(l[4::3])


# In[40]:


print(l)


# In[41]:


print(l[8:2:-2])


# In[43]:


print(l[2:8:2])


# In[49]:


l=[10,20,30,40,50]
i=0
while i<len(l):
    print(l[i])
    i=i+1


# In[50]:


l=[10,20,30,40,50]
for x in l:
    print(x)


# # printing even number

# In[51]:


l=[1,2,3,4,5,6,7,7,8,9,10]
for x in l:
    if x%2==0:
        print(x)


# In[52]:


l=[1,2,3,4,5,6,7,7,8,9,10]
for x in l:
    if x%3==0:
        print(x)


# In[58]:


l=['abcdefghijklemnk']


# In[59]:


print(l[8:2:-2])


# In[60]:


l=[10,20,30,40,50,60,70,80,90,100,110]


# In[62]:


print(l[8:2:2])


#  
