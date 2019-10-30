#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = grades
    for i in range(len(grades)):
        if grades[i] > 35 and 5 - grades[i]%5 < 3:
            result[i] = grades[i] + (5 - grades[i] % 5)
        else:
            
            result[i] = grades[i]

    tuple(result)

    return result


# In[5]:


grades = [73, 67, 38, 33]
gradingStudents(grades)


# HackerLand University has the following grading policy:
# 
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's grade according to these rules:
# 
# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# For example, grade = 84 will be rounded to 85 but grade = 29 will not be rounded because the rounding would result in a number that is less than 40.
# 
# Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.
# 
# Function Description
# 
# Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.
# 
# gradingStudents has the following parameter(s):
# 
# - grades: an array of integers representing grades before rounding
# 
# Input Format
# 
# The first line contains a single integer, n , the number of students.
# Each line i of the n subsequent lines contains a single integer,grades[i] , denoting student i's grade.
# 
# Constraints
# 
# - $ 1 \leq n \leq 60 $
# - $ 0 \leq grade[i] \leq 100$
# 
# Output Format
# 
# For each grades[i], print the rounded grade on a new line.
# 
# Sample Input 0
# 
# 4
# 73
# 67
# 38
# 33
# 
# Sample Output 0
# 
# 75
# 67
# 40
# 33
# 
# Explanation 0
# 
# <img src = https://s3.amazonaws.com/hr-challenge-images/0/1484768684-54439977a1-curving2.png>
# 
# Student 1 received a 73, and the next multiple of 5 from 73 is 75. Since , the student's grade is rounded to .
# Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
# Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
# Student  received a grade below , so the grade will not be modified and the student's final grade is .

# In[ ]:




