#!/usr/bin/env python
# coding: utf-8

# In[1]:


commasepvalues = input("Input some comma seprated numbers : ")
list = commasepvalues.split(",")
print('List : ',list)


# In[2]:


nstar=5;
for i in range(nstar):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(nstar,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[3]:


wordrev = input("Input a word to reverse: ")

for char in range(len(wordrev) - 1, -1, -1):
  print(wordrev[char], end="")
print("\n")


# In[5]:


print("WE, THE PEOPLE OF INDIA, \n\thaving solemnly resolved to constitute India into a SOVEREIGN, ! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens")


# In[ ]:




