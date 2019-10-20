#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        print("#"*i)
if __name__ == '__main__':
    n = int(input())

    staircase(n)


# In[ ]:




