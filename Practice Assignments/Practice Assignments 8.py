# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 08:25:35 2022

@author: Joseph Bonadeo
"""

## Coding challenge 1##
## Create a program which simulates a dice roll with two die using hte random module
## each die has the numbers from 1 to 6
## The expected output below shows what should print out for each roll of the dice
## Notice the difference when I roll 8? You must incorporate logic to change the output statement 
## when an 8 is rolled

## Hint ##
## Lookup the Random module from the link on the notes page, and research random.choice(seq).  The seq is a list of numbers for a single die. 



""" Expected output
you rolled a 10, Die1 was 4, Die2 was 6
you rolled an 8, Die1 was 2, Die2 was 6
"""
### Code goes below ###

import random 

mylist = [1,2,3,4,5,6]
mylist2 = [1,2,3,4,5,6]

Die1 = random.choice(mylist)
Die2 = random.choice(mylist2)
add = Die1 + Die2

if add  ==8:
    print(f"you rolled an {add}, Die1 was {Die1}, Die2 was {Die2}")
elif add ==11:
    print(f"you rolled an {add}, Die1 was {Die1}, Die2 was {Die2}")
else:
    print(f"you rolled a {add}, Die1 was {Die1}, Die2 was {Die2}")

## Coding challenge 2##

#Review the documentation top use yfinance
##    https://pypi.org/project/yfinance/

## We are going to query Yahoo finance for data on stocks.
## In order to use this module in Anaconda, you must first install it. Using a 
## terminal in Anaconda, enter the phrase below without the #

# conda install -c conda-forge yfinance


# Once Installed, import the yfinance package.
# Get input on a ticker symbol from user
# set the input as the ticker symbol for yfinance using the .Ticker method and assign it to a varible
# You should be able to print the varible.info and receive a dictionary of ticker items

### Code goes below ###

import yfinance as yf

myinput = input("Please enter a stock symbol: ")
myStock = yf.Ticker(myinput)

for key in myStock.info:
    print(key, ':', myStock.info[key])
print("\n")



random.seed(10)
myGuess = int(input("Please enter a number between 1 and 10: "))
myNumber= random.randrange(1, 10)
if myGuess == myNumber:
    print(f"Congratulations, you guessed the secret number {myNumber}")
else:
    print (f"Sorry, your guess was incorrect, the secret number was {myNumber}")
    

# Choose the secret number
myNumber = 5

# Ask the user to guess the secret number
myGuess = int(input("Please enter a number between 1 and 10: "))

# Check if the user's guess is correct
if myGuess == myNumber:
    # If the user's guess is correct, print a congratulatory message
    print(f"Congratulations, you guessed the secret number {myNumber}")
else:
    # If the user's guess is incorrect, print a message with the correct number
    print (f"Sorry, your guess was incorrect, the secret number was {myNumber}")
