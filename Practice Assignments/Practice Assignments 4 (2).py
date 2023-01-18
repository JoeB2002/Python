# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:24:30 2022

@author: Joseph Bonadeo
"""
############Challenge 1 #########
# suppose you wanted to add a sequence of numbers together and get a sum.
# the sequence is made of contiguous numbers,
# write code to sum a sequnce of numbers.  Ask a user a starting number and how
#many consecutive numbers to sum together
## HINT: Initialize a variable to hold the total by first assigning the 
#variable to 0. Then do your math and assign the total to it. 

""" Expected Output
What is your starting number? 1
How many numbers in the sequence? 10
The sum of nmbers from 11 to 10 is 55

"""

###########Challenge 1 Code Below ########################

        
total = 0
start = int(input("What is your starting number?"))
end = int(input("How many numbers in the sequence?"))
while start <= end:
    total = total + start
    start += 1
print ("The sum of numbers from", start, "to", end, "is", total)

print('\n')

############Challenge 2 #########

#Suppose you have a list of cars named cars. 
# Write a short piece of code using a for loop to print out the entire list
  
""" Expected output
Ford
Chevrolet
Dodge
Range Rover
BMW
Mercedes
Toyota
Nissan
Kia
"""

###########Challenge 2 Code Below ########################

print("\n")    
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]

    
i=0
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]
while i < len(cars):
    print(cars[i])
    i+=1
    
print('\n')    
    
############Challenge 3 #########    
# Once you get the loop to print out the entire list, the challenge is to
#start with the first car manufacturer in the list and print out every other 
# manufacturer    
#HINT: use the range() function to help you    
""" expected Output

Ford
Dodge
BMW
Toyota
Kia
"""

###########Challenge 3 Code Below ########################

print("\n")
i=0
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]
while i < len(cars):
    print(cars[i])
    i+=2
    
print('\n')

############Challenge 4 #########    
#Now use the same code as challenge 3 and start from the second manufacturer
# and print out every other manufacturer
    
""" expected output
Chevrolet
Range Rover
Mercedes
Nissan
"""

###########Challenge 4 Code Below ########################

print("\n")
i=1
cars=["Ford", "Chevrolet", "Dodge", "Range Rover", "BMW", "Mercedes", "Toyota", "Nissan", "Kia"]
while i < len(cars):
    print(cars[i])
    i+=2
    
print('\n')

############Challenge 5 #########  

# using a for loop, print out a set of even numbers from 0 to 20, then reuse the code to print a set of odd nbumbers from 0 to 20

"""Expected Output - Even
2
4
6
8
10
12
14
16
18
20


Expected Output Odd
1
3
5
7
9
11
13
15
17
19

"""

###########Challenge 5 Code Below ########################    
    
print("\n")
for number in range(0,21,2):
    print(number)
    
print('\n')    
    
for number in range(1,20,2):
    print(number)

