#!/usr/bin/env python
# coding: utf-8

# In[37]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    diag_1 = []
    diag_2 = []
    
    for i in range(n):
        diag_1.append(arr[i][i])
        diag_2.append(arr[i][n-1-i])
    
    return abs(sum(diag_1) - sum(diag_2))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
diagonalDifference(arr)


# In[ ]:





# In[ ]:




