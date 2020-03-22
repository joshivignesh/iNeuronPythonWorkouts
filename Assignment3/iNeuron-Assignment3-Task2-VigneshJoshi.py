#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

x = np.array([1, 2, 3, 5])
N = 3
np.vander(x, N)


# In[4]:


np.vander(x, increasing=True)

