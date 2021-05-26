#!/usr/bin/env python
# coding: utf-8

# In[4]:


n1=int(input('enter first number:'))
n2=int(input('enter seond number:'))
n3=int(input('enter third number:'))
if n1<n2 and n2<n3:
    print('smaller number n1:')
elif n2<n3:
        print('smaller number n2:')
else:
    print('biggest number n3:')


# In[3]:


n1=int(input('enter first number:'))
n2=int(input('enter second number:'))
if n1<n2:
    print('smaller number n1:')
else:
    print('bigger number n2:')


# In[5]:


num = int(input("Enter a number: ")) 
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))


# In[10]:


num = int(input("Enter a number: ")) 
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))


# # write a program to check wheather given number is in between 1 and 100?
# 

# In[14]:


n=int(input("enter the number"))

if n>100:   #statement to check whether less than 100 or not

   print(n,"is less than 100")

elif n==100:
    print('the given number equal to 100')
else:
    print('n is greater than 100')


# In[22]:


n=int(input("enter the number"))
if n>100:
    print('n is leethan 100')
elif n==100:
    print('n is equal to 100')
else:
    print('n is greater than 100')

