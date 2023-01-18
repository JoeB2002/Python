# -*- coding: utf-8 -*-

"""
Welcome to the proactice coding portion of the Mideterm for INFO-233

Directions:
    
    1. Read through all of the comments in this file and follow the directions exactly. 
    2. Your code's output must match the expected output from each problem.
    3. Original work only. Your work must be your own. 
    4. When completed, save the file as info-233-midterm_practice _yourlastname and uipload it the assignment in Canvas
    5. Good luck and relax. Use all of the resources you have. 



"""




############################################################ Problem 1  ############################################################################################
## This problem covers the concepts of:
##      1. dictionaries
##      2. iteration using for loops
##      
## Given the dictionary below, 
##      1.append the key 'New York City Queens' and the value 'New York Mets',
##      2. Print out the contents of the ditcionary one key:value pair per row
##      4. Display all of the cities  contained in the dictionary to the screen one item per row  and ask a user to choose one city to delete and delete the dictionary entry
##      5. Test the dictionary to see if the delete was successful 
##      5. Print out the contents of the ditcionary one key:value pair per row



###  Problem 1 Code goes here

delted_mlbTeam = input("Which do you hate the most to delete?")

mlbTeams ={
    'Baltimore': 'Baltimore Orioles', 
    'Boston': 'Boston Red Sox', 
    'New York City Bronx': 'New York Yankees', 
    'St. Petersburg': 'Tampa Bay Rays', 
    'Toronto': 'Toronto Blue Jays', 
    'Chicago': 'Chicago Cubs', 
    'Cleveland': 'Cleveland Indians', 
    'Detroit': 'Detroit Tigers', 
    'Kansas City': 'Kansas City Royals', 
    'Minneapolis': 'Minnesota Twins', 
    }

mlbTeams.pop(delted_mlbTeam)

for mlbTeam in mlbTeams:
    print(mlbTeam,mlbTeams[mlbTeam], sep = ':')








####################################################################################################################################################################



############################################################ Problem 2  ############################################################################################
## This problem convers the concepts of:
##      1. function definition
##      2. Passing variable to and from functions
##      3. fstrings
##      
## Create code which
##  1. Asks a user to input a number
##  2. Take the number and pass it to a function called sqIt()
##  3. Within the function, square the number and return the value to the main program
##  4. Using an fstring, Printout the squared value to the screen as shown in the expected output

""" Expected Output


Please enter a number to square: 23
the numeber you entered was 23, and its square is 529

"""


### Problem 2 Code goes here

def sqIt(numbers):
    square = numbers*numbers
    
    return square

numbers = int(input("Please enter a number to square: "))
square = sqIt(numbers)


print(f"The number you entered was {numbers} and its square is {square}")







    
####################################################################################################################################################################