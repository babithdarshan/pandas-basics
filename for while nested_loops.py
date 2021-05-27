#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=1
while x<=10:
    print(x)
    x=x+1


# In[5]:


name= ''
while name != 'sunny':
    name=input('enter your favourite heroine')
print('thanks for conformation')


# In[13]:


name=''
while name !='ameesha':
    name=input('enter your favourite heroine')
    

print('thanks for your valuable time')


# # break(jumping statements
# 

# In[14]:


name=''
i=0
while name !='ameesha':
    name=input('enter your favourite heroine')
    i=i+1
    if i==10:
        print('sorry maximum attempts completed')
    

print('thanks for your valuable time')


# In[17]:


name=''
i=0
while name !='sathish':
    name=input('enter user name:')
    i=i+1
    if i==10:
        
        print('your maximum attempts compelted please try after some time')
        break
print('thanks for conformation')
    


# In[24]:


for i in range(10):
    print('hello',end='')


# In[ ]:





# In[ ]:




