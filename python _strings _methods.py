#!/usr/bin/env python
# coding: utf-8

# In[12]:


t=('10','20','30')
s=''.join(t)


# In[13]:


print(s)


# In[14]:


s='learnining PYTHON is very easy'
print(s.upper())


# In[15]:


s='learnining PYTHON is very easy'
print(s.lower())


# In[16]:


s='learnining PYTHON is very easy'
print(s.swapcase())


# In[17]:


s='learnining PYTHON is very easy'
print(s.title())


# In[18]:


s='learnining PYTHON is very easy'
print(s.capitalize())


# In[22]:


print('sathish1990'.isalnum())


# In[23]:


print('sathish1990'.isalpha())


# In[25]:


print('sathish'.islower())


# In[27]:


print('SATHISH'.isupper())


# In[33]:


print('Learning Python Is Very Easy'.istitle())


# In[43]:


s=input('enter any character:')
if s.isalnum():
    print('Alpha numeric character')
    if s.isalpha():
        print('All characters')
        if s.islower():
            print('all lower numbers')
        else:
            print('its a digit')
elif s.isspace():
    print('its space character')
else:
    print('its special symbol')


# In[44]:


s='The cost of the product is 123.45 per piece'
l=s.split()


# In[46]:


print(l)


# In[47]:


print(l[6],l[7])


# In[49]:


s='1990'
print(s.islower())
print(s.isalnum())
print(s.isalpha())


# In[ ]:




