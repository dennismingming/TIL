#!/usr/bin/env python
# coding: utf-8

# In[74]:


#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    am_pm=0
    if s == "12:00:00PM":
        return "12:00:00"
    elif s == "12:00:00AM":
        return "00:00:00"

    elif s[-2] == "P" and s[0:2] == "12":
        am_pm = 0

        
    elif s[-2] == "A"and s[0:2] == "12":
        am_pm = -12
        print(s[0:2])
    elif s[-2] == "P":
        am_pm = 12
    elif s[-2] == "A":
        am_pm = 0
    s = s[0:-2]
    ti = s.split(":")
    ti = list(map(int,ti))
    #if ti[0]==12:
        #am_pm=-12
    if am_pm == 12 or am_pm == -12:
        ti[0] = ti[0] + am_pm

    if ti[0]<10:
        #ti[0] = str(ti[0])
        ti[0] = "0"+str(ti[0])
    if ti[1]<10:
        ti[1]="0"+str(ti[1])
    if ti[2]<10:
        ti[2]="0"+str(ti[2])
    
    result = list(map(str,ti))
    result = ":".join(result)

    
    return result
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()


# In[ ]:





# In[ ]:




