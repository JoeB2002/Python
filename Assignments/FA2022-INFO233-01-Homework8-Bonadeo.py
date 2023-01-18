# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 18:46:14 2022

@author: Joseph Bonadeo
"""

# Create a rock,paper, scissor game in python
# The game rock, paper , scissor is a game with two people , each slecting either rock, paper or scissor. The outcome is decided as follows:
# Rock beats scissors, paper beats rock and scissors beats paper.  A tie occurs when both players select the same item.
# in this version of the game, player 1 playes against a computer opponent.
# the computer opponent randomly selects one of the choices, Player 1 is prompted to enter rock, paper or scissor. Once player 1 enters a choice,
# both seletions are displayed and the outcome is chosen. 

## your code must contain the following:
# 1. ask a user the select either rock, paper or scissor
# 2. If anything else is inputted, repeat the selection (i.e. the person types in tree, present the selection again)
# 3. The computer randomly selects it's choice
# 4. A function which decides the outcome by accepting two variables, decides the winner and returns a message to the main program
# 5. The outcomes are printed to the screen. Format the print statment as shown in the expected output 
#  The expected output shows the output messages. Outcomes are random in this program

## HINT: ###
# Don't forget it is easier to test something if the case of the input is set in advance
## research the use of the while not in loop to ensure the user enters only what we want, see requirement 2 above. 

""" Expected Output
Please enter rock, paper or scissor: rock
Player's choice: rock, Computer's choice: paper, Computer Wins!


Please enter rock, paper or scissor: paper
Player's choice: paper, Computer's choice: scissor, Computer Wins!

Please enter rock, paper or scissor: scissor
Player's choice: scissor, Computer's choice: scissor, It is a Tie!

Please enter rock, paper or scissor: rock
Player's choice: rock, Computer's choice: scissor, Player Wins!

"""
## Problem code goes below:Roc
    
import random 

        
userChoice = input("Please enter rock, paper or scissor: ")
userChoice = userChoice.lower()
computer = ["rock", "paper", "scissor"]
computer_choice = random.choice(computer)

while userChoice != "rock" and userChoice != "paper" and userChoice != "scissor":
     userChoice = input("Please enter rock, paper or scissor: ")
     userChoice = userChoice.lower()


def winner(userChoice, computer_choice):
    if userChoice == computer_choice:
        return("It is a Tie!")
    elif userChoice == "rock":
        if computer_choice == "scissor":
            return("Player Wins!")
        else:
            return("Computer Wins!")
    elif userChoice == "paper":
        if computer_choice == "rock":
            return("Player Wins!")
        else:
            return("Computer Wins!")
    elif userChoice == "scissor":
        if computer_choice == "paper":
            return("Player Wins!")
        else:
            return("Computer Wins!")
            
print(f"Player's choice: {userChoice}, Computer's choice: {computer_choice}, {winner(userChoice, computer_choice)}" )




## Second problem ####

## Continue your work with the yfinance package. Now that you have a ticker and can display the dictionary,
## Pick out the following
## 1. The Short Name of the company
## 2. The currency the stock trades in
## 3. Current price for any stock
## 4. The 52 Week High 
## 5. The 52 Week Low
## Finally implement an exception handling scheme where if a user inputs a non-existant stock 
## Symbol    

import yfinance as yf

isReal = False
while isReal == False:
    myinput = input("Please enter a stock symbol: ")
    myStock = yf.Ticker(myinput)
    
    if myStock.info['regularMarketPrice'] != None:
        isReal = True
    else:
        print("This ticker does not exist")

financedict = {}
financedict.update(myStock.info)

print(f"\nThe Short Name of the compay: {financedict['shortName']} \nThe currency the stock trades in: {financedict['currency']} \nCurrent price is: {financedict['regularMarketPrice']} \nThe 52 Week High is: {financedict['fiftyTwoWeekHigh']} \nThe 52 Week Low is: {financedict['fiftyTwoWeekLow']}")