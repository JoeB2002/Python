# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 12:46:54 2022

@author: Joseph Bonadeo
"""
# Course: Introduction to Programming (INFO-233)
# Student Name: # Joseph Bonadeo 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

#########################
# Problem 1: Hello World!
#########################

"""This problem is to ensure that you are properly set up with a Python
# programming environment. After opening your environment
# Create a print statment to print Two words together as one line using two separate arguments in one print statment
 
# After your programe runs, recreate this program , but now print "Hello World!" one letter at a time separated by three
#dots bewteen each letter so your output will look like the sample below

#  Sample output - output should not have the "#" 
#########################
Hello World!
H...e...l...l...o... ...W...o...r...l...d...! 

######################### """


#########################
#HINT: research the sep parameter in print()
#########################


# YOUR CODE GOES HERE - Problem 1

print("Hello" + " World!")
print("H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!", sep = "...")


#########################
# #Problem 2: working with Variables and math
#########################

""" This problem will look at using variables to represent the value. you will assign values to variables
and perform some simple math to get an answer

In the first part of this problem...
We are planning to drive from Ramapo to Daytona Beach FL. How many times should we stop to for fuel along 
the way ? Given the total miles for the trip is  1,044.5 mi. Our car gets pretty crappy mileage on the highway so let's assume we get 22 mpg
and our gas tank can hold 18 Gallons.  """

#Constraints 
""" 
1.  Your formula to calculate the answer should only perform math on variables, numbers in the formula
cannot be used.
2.  Your final answer must be a whole number since you cannot stop for a fraction. 
3. You must include comments in  your code to explain the math involved. 
"""
#########################
# #HINT: Research the round()
#########################


# YOUR CODE GOES  HERE - Problem 2 part 1

totalMiles = 1044.5
mpg = 22
gastank = 18

MaxMiles = mpg * gastank
numstop = round(totalMiles/MaxMiles)
print (numstop)

#I first put down all the important key variables needed.
#I then multiplied mpg and gastank, due to finding out what the maxmiles of the car is.
#Once all that is done I used the round feature to allow my number to be the closest integer. Which elimates it from being a decimal. It will then give me a whole number.
#I then divided (Floating-point division) the total miles and max miles, which will then allow us to see how many times should we stop for fuel along the way.
#Lastly I wanted to print out the numstop, which allowed to display allowed me to display the total number of stops for fuel.

""" For the second part of this problem set, we want to explore using different vehicleswith different MPG - modify the problem to ask
the user the MPG of the vechicle 
"""

#Constraints 
""" 
1.  Your formula to calculate the answer should only perform math on variables, numbers in the formula
cannot be used.
2.  Your final answer must be a whole number since you cannot stop for a fraction. 
3. You must include comments in  your code to explain the math involved. 
"""

#########################
#HINT - Use you knowledge of round() and also research the use of input()
#########################

# YOUR CODE GOES HERE - Problem 2 part 2

totalMiles = 1044.5
gastank = 18

mpg = input("What is the vehicles Miles Per Gallon? ")
MaxMiles = (int(mpg)) * gastank
numstop = round(totalMiles/int(MaxMiles))
print (numstop)

#I chose the varibales I needed for the math part which was totalmiles and gastank 
#This allowed me to multiple the mpg to the gastank which then proudced the output of my maxmiles
#I then used the input funtion to convert the line into a string. Eliminating a floating-point number.
#Also, I converted the totalmiles into a whole number by making it an integer with in int() statement
#While doing this it allowed me to see how many stops were needed by taking the totalMiles and diving the maxmiles. 
#Once using the round tool again(which allowed me to get to the closest integer), it allowed me to get my answer into a whole number which then allowed the input data listed above into an integer. 

## Complete your coding and submit a copy of this file saved as  FA2022-INFO233-01-Homework1-Your_Last_Name
