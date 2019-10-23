#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    sumation = 0
    zero = arr.count(0)
    positive = -zero
    negative = 0
    for i in range(len(arr)):
        if abs(arr[i]) != arr[i]:
            negative += 1
        elif abs(arr[i]) == arr[i]:
            positive += 1
    print(round(positive/len(arr),6))
    print(round(negative/len(arr),6))
    print(round(zero/len(arr),6))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


# In[ ]:




