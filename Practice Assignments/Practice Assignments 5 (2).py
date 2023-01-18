# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:57:55 2022

@author: Joseph Bonadeo
"""
## Challenge 1 #####################
# Create a function which asks a user to type a season, spring, summer , fall, winter.
# Depending on which season they type, print a seasonal statement. CAll the function
# by passing the variable holding the user's season. Please ensure the inout is not case-sensitive. 
# For example Winter is the same as winter is the same as WINTER.
# also inlcude a print statement if the user entered a word which is not a season. 
# Output messages as follows
# for Spring,  "April showers bring May Flowers"
# For Summer, "It's Beach time"
# For Fall, "It's time for Turkey Day"
# For Winter, "Snowman Season"
# For an incorrect season, "Plese enter either Spring, Summer, Winter or Fall"

"""
Expected Output

please enter a season for a message SPRING
April showers bring May Flowers

please enter a season for a message Spring
April showers bring May Flowers

please enter a season for a message spring
April showers bring May Flowers

please enter a season for a message pre spring
Plese enter either Spring, Summer, Winter or Fall

"""

## Challenge 1  code goes here#####################
def spring():
    print('April showers bring May Flowers')
def summer():
    print("It's Beach time")
def fall():
    print("It's time for Turkey Day")
def winter():
    print('Snowman Season')
def inputerror():
    print('Please input either Spring, Summer, Winter, or Fall')
    
def UserInput():
    uinput=input('Please enter a season for a message: ')
    luinput=uinput.lower()
    if luinput=='spring':
        spring()
    elif luinput=='summer':
        summer()
    elif luinput=='fall':
        fall()
    elif luinput=='winter':
        winter()
    else:
        inputerror()
        
UserInput()
        

    
            


## Challenge 2 #####################
# Error Handling
# Practice error handling by writing a function to print the square of an integer and return the square
# to the main part of the program and print it out. If the user should enter a decimal (float) in error,
# let the user know to only enter a whole nmuber (integer) the program should run and not generate any 
#system errors. 

""" Expected Output
Please enter an integer to get its square root: 10
The square of  10 is 100

Please enter an integer to get its square root: 2.3
Your entry was not a whole number, please enter an whole number

Please enter an integer to get its square root: go away
Your entry was not a whole number, please enter an whole number


"""

## Challenge 2  code goes here#####################

def main():
    sr()
    
def sr():
    try:
        uninput = input('Please enter integer to get its square root: ')
        for i in uninput:
            uninput = int(uninput)
            squared = uninput **2
            print(squared)
    except ValueError:
            print('Please enter a whole number')
            
main()

  

## Challenge 3 #####################
# Combining what we learned
# we've learned a lot over the last few weeks. Let's put that to use
# Create a code block which consists for a function to average grades
#The function should be able to take any number of grades
# Caluclate the average of the grades and return it to the main prgram
# in the main program use the average returned and test it to determine a letter grade
# 90 and up is A, 80 to 89 is a B, 70 to 79 is a C 60 to 69 a D and below 60 is an F.

##HINT, you tested for grades before, right, reuse the code.  Code resuse is one of the best ways to 
#things done quickly

""" Expected Output  given 100,100,70,60
Your grade averages is 82.5
which is a B
"""


## Challenge 3  code goes here#####################

def grade_It(grade):
    if grade >= 90:
        gradeoutput='A'
    elif grade >= 80:
        gradeoutput='B'
    elif grade >= 70:
            gradeoutput='C'
    elif grade >= 60:
                gradeoutput='D'
    else:
        gradeoutput='F'
    return gradeoutput
    
def averages (*args):
    grade_Avg = 0
    grade_sum = 0
    count = 0
    for arg in args:
        count +=1
    for average in args:
        grade_sum += average
    
    grade_Avg = grade_sum/count
    return grade_Avg

myAvg = averages (100,100,70,60)
myGrade = grade_It(myAvg)
print (f"Your average is {myAvg:,.2f}")
print(f"which is a {myGrade}")
