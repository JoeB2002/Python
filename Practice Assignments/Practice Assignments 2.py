# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 08:30:49 2022

@author: Joseph Bonadeo
"""

# Course: Introduction to Programming (INFO-233)
# Student Name: # you

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

#Let's look at how to make decisions in Python
# We are going to create a guessing game


########################## Challenge 1 ################################
# Variable assignment
# Assign a secret number to a variable 
# Assign a variable to an input statement asking a user to input a guess between a range of numbers of which your secret number is included

""" Expected Output

Please enter a guess number between 0 and 100:
"""

## Challenge 1 Code  below ##################


SecNum = 2

SecNum = input(str("Guess a number between 0 and 100? "))
print(SecNum)


########################## Challenge 2 ################################
# Comparing the input and the secret number.
# Since this is a simple comparision of two numbers, we can use if / else to compare them
# if your number equals the secret number, print a message letting the user know the numbers match. 
# if the number does not equal the secret number, let the user know their guess was incorect

""" Expected output given my secret number is 53
Please enter a guess number between 0 and 100: 50
Sorry your guess did not match the number
"""

## Challenge 2 & 3 Code  below ##################

SecNum = '2'
guessNum = input(str("Guess a number between 0 and 100? "))

if guessNum == SecNum:
    print("Yes! You got the number corretly! ")
else:
    print("Sorry, that's incorrect")





########################## Challenge 3 ################################
## So the program doesn't exactly work, specifically if the guess matches the secret number
# the program still puts out the message that the numbers do not match. 
# What is the issue?
#fix the code so the if statementfunctions correctly 
# HINT: Look into the functions input(), What is the type of data for an input variable?

""" Expected Output
Please enter a guess number between 0 and 100: 53
Congratulations, the numbers matched  Great job!!

"""

########################## Challenge 4 ################################

### Now it is your turn, create code which will determine the letter grade of an inoutted grade
"""

This is the grade ranges we are using in the program

90.0-100 A 
80.0-89.9 B
70.0-79.9 C
60.0-69.9 D
00.0-59.9 F 


Expected Output

Please enter a grade to analyze. This can be a whole number or a decimal: 92
92.0 is an A

"""
## Challenge 4 Code  below ##################


score = float(input("Please enter your grade: "))

if score >= 90:
    print(score, "is an ","A")
elif score >= 80:
    print(score, "is an ","B")
elif score >= 70:
    print(score, "is an ","C")
elif score >= 60:
    print(score, "is an ","D")
else:
    print(score, "is an ","F")
    


########################## Challenge 5 ################################

#  Let's play with some string 
#using the string alphabet below, Ask a user to enter a number and your program will display the letter in the alphabet 
# which corresponds to the number ##HINT: be careful of how to select a character. Test it with the number 1, did the correct letter appear?
""" Expected output
Please enter number to find out the corresponding letter in the alphabet:1
The letter in position 1 is a

"""
alphabet = 'abcdefghijklmnopqrstuvwxyz'

## Challenge 5 Code  below ##################


letter_guess = int(input("Please enter number to find out the corresponding letter in the alphabet: "))
print("The letter in position", letter_guess, "is", alphabet[letter_guess-1])


########################## Challenge 6 ################################

#Now take the code from above and modify it to ask the user the starting position and how many characters after the starting to show
# HINT: remember the offset in slicing, the second value is the stop position, not the length
""" Expected Output
Please enter number to find out the corresponding letter in the alphabet:5
Please enter number of letters to display in a row:10
The letter in position starting at 5 and continuing for  10 is efghijklmn

"""
## Challenge 6 Code  below ##################


letter = int(input("Please enter number to find out the corresponding leter in the alphabet:"))
mynum = int(input("Please enter number of letters to display in a row:"))
print("The letter in position starting at", letter, "and continuing for ",mynum, "is" ,alphabet[letter-1:letter+mynum-1])