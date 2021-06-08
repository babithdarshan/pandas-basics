#!/usr/bin/env python
# coding: utf-8

# In[1]:


s={10,50,40,20,25,0,5}


# In[7]:


print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


# In[8]:


s


# In[13]:


if len(s)!=0:
    print(s.pop())


# In[14]:


s


# In[15]:


s={10,20,30,40,60,10,10,10,10}


# In[16]:


type(s)


# In[17]:


s


# In[18]:


s={10,20,30,40,50,60,70,80,90,70,70}
while len(s) != 0:
    n=s.pop()
    print('sending mobile numbers:',n)


# In[20]:


s={10,20,30,10,20,30,40,50,60,70,70,80,10,20,30,40,50}


# In[22]:


s={10,20,30,10,20,30,40,50,60,70,70,80,10,20,30,40,50}


while len(s) !=0:
          n=s.pop()
          print('sending sms to the mobile number:',n)


# In[25]:


s.discard(20)


# In[27]:


print(s)


# In[28]:


s={10,20,30,10,20,30,40,50,60,70,70,80,10,20,30,40,50}


# In[29]:


print(s)


# In[31]:


s.discard(10)


# In[32]:


print(s)


# In[33]:


s={10,20,30}
s.discard(20)
s.discard(50)
s.discard(20)
s.discard(20)
print(s)


# In[34]:


s.clear()


# In[35]:


print(s)


# In[39]:


x={10,20,30,40}
y={30,40,50,60}
print(x.union(y))


# In[42]:


x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y))


# In[43]:


x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))


# In[44]:


x={10,20,30,40}


# In[45]:


print(10 in x)


# In[46]:


print(50 in x)


# In[47]:


print(50 not in x)


# In[53]:


s= {2**x for x in range(1,6)}


# In[54]:


print(s)


# In[56]:


s1={10,20,30}
s2={40,50,60}
print(x.symmetric_difference(y))


# In[76]:


s1={10,20,30}
s2={20,10,30}
print(s1==s2)


# In[66]:


print(id(s1))
print(id(s2))


# In[71]:


s={x*x for x in range(1,6)}


# In[72]:


print(s)


# In[ ]:





# In[ ]:





# In[81]:


w=input('enter any word to search for vowels:')
s=set(w)
v={'a','e','i','o','u'}
print(s)


# In[ ]:




