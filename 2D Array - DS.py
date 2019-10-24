#!/usr/bin/env python
# coding: utf-8

# In[30]:


#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
# Complete the hourglassSum function below.


def hourglassSum(arr):
    copy_mat = [[0,0,0],[0,0,0],[0,0,0]]    
    temp_memo = -100000
    result=0
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            sum_temp = 0
            for ii in range(3):
                for jj in range(3):
                    if ii == 1 and jj == 2 :
                        copy_mat[ii][jj] = 0
                    elif ii == 1 and jj == 0:
                        copy_mat[ii][jj] = 0
                    else:
                        copy_mat[ii][jj] = (arr[i+ii][j+jj])
                    sum_temp += copy_mat[ii][jj] 
            temp_memo = temp_memo if temp_memo > sum_temp else sum_temp
            result = temp_memo
    return result


# In[31]:


arr1 = [[1,1,1,0,0,0],
[0,1,0,0,0,0],
[1,1,1,0,0,0],
[0,9,2,-4,-4,0],
[0,0,0,-2,0,0],
[0,0,-1,-2,-4,0]]
arr2 = [[0, -4, -6, 0, -7, -6,],
[-1, -2, -6, -8, -3, -1],
[-8, -4, -2, -8, -8, -6],
[-3, -1, -2, -5, -7, -4],
[-3, -5, -3, -6, -6, -6],
[-3, -6, 0, -8, -6, -7]]
hourglassSum(arr2)

