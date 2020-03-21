#!/usr/bin/env python
# coding: utf-8

# In[5]:


arr=[]
for x in range(1999, 3201):
    if (x%7==0) and (x%5!=0):
        arr.append(str(x))
print (','.join(arr))


# In[7]:


firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print (lastname + " " + firstname)


# In[8]:


pi = 3.1415926535897931
radius= 6.0  
Volume= 4.0/3.0*pi* radius**3
print('The volume of the sphere is: ',Volume)

