#!/usr/bin/env python
# coding: utf-8

# In[ ]:




s='learning python is very easy'
print(s.find('y'))
print(s.rfind('p'))
print(s.index('d'))
print(s.rindex('y'))find and rfind bothr are same
# # program to display all positions of substring in the given main string?
# 

# In[11]:


s=(input('enter main string:'))
subs=(input('enter substring:'))
n=len(s) 
pos=0
count=0
while True:
    i=s.find(subs,pos,n)
    if i== -1:
        break
    else:
        print('found at index:',i)
        pos=i+len(subs)
print('the total number of occurencess:',count(subs))
print('the total number of occurences:',s.count(subs,4,10))


# In[5]:


s='learning python is very easy'
print(s.find('y'))
print(s.rfind('y'))
print(s.index('y'))


# In[13]:


s= 'darshanala'
s.replace('dar','xx')


# In[14]:


s='learning python is very difficult'
s1=s.replace('difficult','easy')


# In[15]:


s


# In[16]:


s1


# In[30]:


s= 'ab ab ab ab ab'
s1=s.replace(' ','')


# In[19]:


s1


# In[31]:


print(s1)
print(s1)


# In[32]:


s


# In[33]:


s1


# # write a script to find the number spacess to present in the given string

# In[34]:


s= 'ab ab ab ab ab'
s1=s.replace(' ','')
print(len(s)-len(s1))


# In[35]:


s='durga software solutions'
l=s.split()
print(l)


# In[40]:


s.split('-')
print(s)


# In[41]:


for x in l:
    print(x)


# In[42]:


s= '01-08-2020'
s.split('-')
print(s)


# In[ ]:




