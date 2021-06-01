#!/usr/bin/env python
# coding: utf-8

# In[3]:


city=input('enter your city name:').lower().strip()
if city == 'hyderabad':
    print('helllo hyderbadi')
elif city =='chennai':
    print('hello vanakkam')
elif city == 'karnataka':
    print('hello subodhayam')
else:
    print('you have entered city is invalid')


# In[9]:


s='learning python is very easy'
print(s.find('python'))
print(s.rfind('python'))


# In[45]:


s='learning python is very easy'
print(s.find('python'))


# In[23]:


print(s.find('15,25'))


# In[33]:


s='learning i is very easy'
print(s.rfind('15,25'))


# In[44]:


s1='learning i is very easy'
print(s1.find('e',0,10))

