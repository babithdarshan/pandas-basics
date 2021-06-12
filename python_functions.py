#!/usr/bin/env python
# coding: utf-8

# In[7]:


def wish(ravi):
    return('good morning')
wish('ravi')


# In[18]:


def calc(a,b):
    print('the sum:',a+b)
calc(10,20)


# In[44]:


def name(ravi):
    print('good morning')
name('ravi')


# In[24]:


for i in range(5):
    print('hello')


# In[31]:


def goodmorning():
    print('hello')
goodmorning()


# In[36]:


def wish(name):
    print('hello {}, good morning'.format(name))
wish('sathish')


# In[39]:


def wish(name):
    print('hello {}, good morning'.format(name))
wish('ravi')
name=input('enter name:')


# In[43]:


def wish(name):
    print('hello {}, good morning have a nice day'.format(name))
wish('sathish')
wish('tarun')
wish('tarun')
wish('babita')


# In[48]:


def squareIt(number):
    print('the square of {} is: {}'.format(number,number**2))
squareIt(2)
squareIt(4)
squareIt(5)


# In[54]:


def add(x,y):
    print('the addition of {} and {} is {}'.format(x,y,x+y))
add(10,20)


# In[59]:


def add(x,y):
    print('the sum of {} and {} is {}'.format(x,y,x+y))
add(10,20)
squareIt(int(input('enter number value:')))


# In[61]:


def add(x,y):
    return(x+y)
result=add(10,20)
print('the sum:',result)


# In[62]:


def add(x,y):
    print('calling add function...')
    return x+y
add(10,20)


# In[71]:


def validate(mobile_number):
    if len(mobile_number) == 10:
        return True
    else:
        return False
mobile_number=(input('enter mobile number:'))
result=validate(mobile_number)
if result == True:


# In[83]:


def even_odd(x):
    if x%2 ==0:
        print('its even number')
    
    else:
        print('its odd number')
even_odd(21)
even_odd(10)
even_odd(2101)
even_odd(int(input('enter some number:')))
           


# In[86]:


def  show(sequence):
    for x in sequence:
        print(x)
show('sathish')
show (range(1,6))


# In[ ]:




