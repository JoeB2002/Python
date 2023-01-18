# -*- coding: utf-8 -*-
"""
Welcome to the Mideterm for INFO-233

Directions:
    
    1. Read through all of the comments in this file and follow the directions exactly. There are extra credit options in probmes 2,3 & 4
    2. Your code's output must match the expected output from each problem.
    3. Original work only. Your work must be your own. 
    4. When completed, save the file as info-233-midterm_yourlastname and uipload it the assignment in Canvas
    5. Good luck and relax. Use all of the resources you have. 



"""



############################################################ Problem 1  ############################################################################################
## This problem covers the concepts of:
##      1. String Slicing
##      2. Len ()
##      3. Fstrings    
## Given the string below, write three lines of code to 
## 1. first display the string on the screen
## 2. Using one fstring, Extract the class name from the string and display it as part of the second sentence 
## 3. Using one fstring, Create the third sentence by calculating how many characters on the screeen

""" Expected Output

This is the midterm for INFO-233
The class I am taking is INFO-233
The original string is 32 characters long

"""
print("\nProblem 1:\n")

### Problem 1 Code goes here

myString = "This is the midterm for INFO-233"
print(f"{myString}")
print(f"The class I am taking is {myString[24:]}")
print(f"The original string is {len(myString)} characters long")


####################################################################################################################################################################






############################################################ Problem 2  ############################################################################################
## This problem covers the concepts of:
##      1. Iteration using For loops
##      2. List creation
##      3. Data types
## Create two empty lists:
## iterate through a range of 25 numbers from 1 to  25 and add them to the first list
## Iterate through a range of 25 numbers from 26 to 50 and add them to the second list
## print out both lists and their types



""" ***************** Extra Credit is available if you complete this problem using only 1 loop to iterate over all 50 numbers to generate the expected output*****************"""

""" Expected Output

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] <class 'list'>
[26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] <class 'list'>

"""
print("\nProblem 2:\n")

### Problem 2 Code goes here


list1 = []
for j in range (0,26):
    list1.append(j)
print(list1,type(list1))


list2 = []
for j in range (26,51):
    list2.append(j)
print(list2,type(list2))



####################################################################################################################################################################







############################################################ Problem 3  ############################################################################################


### Problem 3
## This problem covers the concepts of:
##      1.Case Conversion
##      2.Function definition
##      3.Passing and returning variables to and from functions
##      4.Iteration 
##      5.Breaking out of a program
##      6.Using Methods

### Create code which:

##  1. contains a function named change_case()
##      A. select option 1 to capitalize the first character of the string
##      B. Select option  2 to capitalize each word in the string
##      C. Select option 3 to set all characters to upper case
##      D. Select option 4 to set all characters to lower case
##      E. Returns the converted string to the main progam
##  2. The main program 
##      A. Asks for input of a string and an option or 'q' to quit
##      B. Asks for input of an option to change the string
##      C. Calls the function  change_case() and passes the two variables to the function
##      D. Prints out the result of the function
##  
    
""" Expected output with option 1 selected. Your program should work for all 4 options

Please enter a string you want to change: this is the string
Please enter an option to change your string
Enter 1 to captialize the first character of your string
Enter 2 to captialize each word of your string
Enter 3 to set all characters of your string to UPPER CASE
Enter 4 to set all characters of your string to lower caseE

Please choose an option: 1
This is the string



"""


print("\nProblem 3 Extra Credit:\n")

### Problem 3 Code goes here

string = input('Please enter a string you want to change:')
print(string)


string2 = input('Please enter an option to change your string')
print(string2)

#def .title(1):
    #print('to captialize the first character of your string')
#def 2():
    #print("to captialize each word of your string")
#def 3():
    #print("to set all characters of your string to UPPER CASE")
#def 4():
    #print('to set all characters of your string to lower case')
    
#def UserInput():
    #uinput=input('Please enter a string you want to change: ')
    #luinput=uinput.lower()
    #if luinput=='spring':
        #spring()
    #elif luinput=='summer':
        #summer()
    #elif luinput=='fall':
        #fall()
    #elif luinput=='winter':
        #winter()
    #else:
        #inputerror()
        
#UserInput()




####################################################################################################################################################################




############################################################ Problem 4  ############################################################################################


## This problem covers the concepts of:
##      1. Dictionaries
##      2. Iteration with loops
##      3. Testing for a key using 'in'
## Given the dictionary below:
##      1. Append the key 'orange' and value 'mango' to the end of the dictionary
##      2. Print out the contents of the ditcionary one key:value pair per row
##      3. Display all of the colors  contained dictionary to the screen one item per row  and ask a user to choose one color to delete and delete the dictionary entry
##      4. Test the dictionary to see if the delete was successful 
##      5. Print out the contents of the ditcionary one key:value pair per row

"""Expected Output

Original Dictionary

yellow : banana
red : apple
purple : grape
green : lime
blue : blueberry

We just added orange to the dictionary

yellow : banana
red : apple
purple : grape
green : lime
blue : blueberry
orange : mango

Please select a color to delete: green

The choice green is no longer in the dictionary

yellow : banana
red : apple
purple : grape
blue : blueberry
orange : mango
"""

""" ***************** Extra Credit is available if you define a function to print the dictionary key:values pairs one line per row and 
**********************call it each time you print the dictionary from your main program *****************"""

### Problem 4 Code goes here
print("\nProblem 4:\n")

fruit_dict={
    'yellow':'banana',
    'red':'apple',
    'purple': 'grape',
    'green':'lime',
    'blue':'blueberry',
     }

for fruit in fruit_dict:
    print (fruit,':',fruit_dict[fruit])
    
print('\n')


fruit_dict.update({"orange": "mango"})
for fruit in fruit_dict:
    print (fruit,':',fruit_dict[fruit])
#(fruit_dict)267

delted_fruit_dict = input("Please select a color to delete: ")

fruit_dict.pop(delted_fruit_dict)
for fruit in fruit_dict:
    print (fruit,':',fruit_dict[fruit])


#############################################################################################################################



## Congratulations, you have complete the coding portion of the midterm please save this file as 
## info-233-midterm_yourlastname and uipload it the assignment in Canvas





























