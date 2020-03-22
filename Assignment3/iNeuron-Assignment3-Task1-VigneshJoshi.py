#!/usr/bin/env python
# coding: utf-8

# In[7]:


def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("We cant divide any value by zero")
except:
    print("Can handle any other general exception")


# In[9]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

sentence_output = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_output:
 print (sentence)

