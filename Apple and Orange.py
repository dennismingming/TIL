#!/usr/bin/env python
# coding: utf-8

# In[24]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_1, count_2 = 0, 0
    
    for i in range(len(apples)):
        if (a + apples[i]) >= s and (a + apples[i]) <= t:
            count_1 += 1
    for j in range(len(oranges)):
        if (b + oranges[j]) <= t  and (b + oranges[j]) >= s:
            count_2 += 1
    
    return count_1, count_2


# In[25]:


s = 7
t = 11
a = 5
b = 15
apples = [-2,2,1]
oranges = [5,-6]
countApplesAndOranges(s, t, a, b, apples, oranges)


# In[ ]:




