# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 07:56:33 2022

@author: Joseph Bonadeo
"""

# Course: Introduction to Programming (INFO-233)
# Student Name: Joseph Bonadeo

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

################################
# Problem 1: Lists
################################

# Build a list (called myList) that contains every year from 2015 to 2022. Write
# the code to verify whether index 1 is (or is not) a leap year. Also verify
# whether the last index of myList is a leap year.
# (Hint: leap years are evenly-divisible by 4)

myList = (2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)

if(myList[1] % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

if(myList[len(myList) - 1] % 4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
########################
# Problem 2: Sets
########################

# Using the two sets below, divBy2 and divBy3, determine which values occur in
# both sets and assign that to a variable called common. Then confirm whether
# common is in fact a subset of both divBy2 and divBy3.

divBy2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
divBy3 = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

common = divBy2.intersection(divBy3)
print(common)
if common.issubset(divBy2) and common.issubset(divBy3):
    print("true")
else:
    print("false")

## Complete your coding and submit a copy of this file saved as  FA2022-INFO233-01-Homework3-Your_Last_Name