#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jump = 0
    loca = 0
    while loca < len(c)-1:
        if c[loca] == 1:
            loca += 1

        else:
            if loca + 2 < len(c)-1 and c[loca + 1] == 0 and c[loca + 2] == 0:
                jump += 1
                loca += 2
                #print("1:",jump,loca)
            elif loca + 2 < len(c)-1 and c[loca + 1] == 1:
                jump += 1
                loca += 1
                #print("2:",jump,loca)
            elif loca+2 < len(c)-1 and c[loca + 1] == 0 and c[loca + 2] == 1:
                jump += 1
                loca += 1
                #print("3:",jump,loca)
            elif loca == len(c)-3:
                jump +=1
                loca +=2
                #print("4:",jump,loca)
            elif loca == len(c)-2:
                jump +=1
                loca +=1
                #print("5:",jump,loca)

    return jump


# In[10]:


c=[0, 0, 1, 0, 0, 1, 0]
jumpingOnClouds(c)


# In[ ]:




