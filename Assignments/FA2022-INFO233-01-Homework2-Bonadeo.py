# Course: Introduction to Programming (INFO-233)
# Student Name: Joseph Bonadeo

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.


#HINT: to output your work to the screen, you must use print()


################################
# Problem 1: Fun With Strings
################################

### Part A ###

# Use substring notation to extract the word "box" from the variable below.

phrase = "Life is like a box of chocolates."

# YOUR CODE GOES HERE

print(phrase[15:18:])
#This one was simple just had to see how many numbers it was to box but had to 
#remember the string STARTS at 0


### Part B ###

# There is a secret code in the variable phrase. It can be found by extracting
# every third character. Write the Python code necessary to extract these
# characters and print the results.

phrase = "I2FNB3F77OVB-PJ2BB3ZQ3BV"

# YOUR CODE GOES HERE

print(phrase[0:len(phrase):3])
#Same as part A just had to make it skip 3 as shown above but wanted to add 
#len so the code knows how long the script is(which help it understand how much to skip)
#FYI you did say we didn't need to comment I just wanted to show you a glimspe
#of it


### Part C ###

# Does any version of the word "new" occur in the variable phrase? Assume this
# means case insensitive. 

phrase = "UnIqUe NeW YoRk"

# YOUR CODE GOES HERE

phrase = phrase.lower()
print(phrase.lower())
if "new" in phrase:
    print("The phrase contains the word you're looking for.")
else: 
    print("The phrase does not contain the word you're looking for.")
#I first made the whole phrase lower(could of been upper as well) because we 
#had to assume this was case sensitive
#Then did an if; else statement due to us needing a boolean type response (true or false)
#FYI: I tried to be a better programmer by writing a complete string instead of 
#saying 'true' or 'false'

########################
# Problem 2: Conditional Statements
########################

# A password must be between 6 and 13 characters. Write Python code to determine
# whether the passwords below meets the necessary length requirements.

### Part A ###

password = 'Nope'

length = len(password)
print("The character length of your password is " + str(length))  
if length <= 6:
    print("Which does meet the requirements of 6 and 13.")
elif length >= 13:
    print("Which does meet the requirements of 6 and 13.")
else:
    print("good")
#I first had to get the length of the password
#Without the variable "length" I would have not be able to do my IF statement
#The reason why I couldn't do it without length is becuase the code needs to
#know if the password is true or false(Boolean)
#Meaning that if I just write "Joe" and the code has if length <=6, >3, etc.
#It wouldn't know long "Joe" is without lentgh 


### Part B ###

password = 'Maybe???'

length = len(password)
print("The character length of your password is " + str(length))  
if length <= 6:
    print("Which does meet the requirements of 6 and 13.")
elif length >= 13:
    print("Which does meet the requirements of 6 and 13.")
else:
    print("good")
#I first had to get the length of the password
#Without the variable "length" I would have not be able to do my IF statement
#The reason why I couldn't do it without length is becuase the code needs to
#know if the password is true or false(Boolean)
#Meaning that if I just write "Joe" and the code has if length <=6, >3, etc.
#It wouldn't know long "Joe" is without lentgh 


### Part C ###

password = 'Wayyyyy Too Longgggg'

length = len(password)
print("The character length of your password is " + str(length)) 
if length <= 6:
    print("Which does meet the requirements of 6 and 13.")
elif length >= 13:
    print("Which does meet the requirements of 6 and 13.")
else:
    print("good")
#I first had to get the length of the password
#Without the variable "length" I would have not be able to do my IF statement
#The reason why I couldn't do it without length is becuase the code needs to
#know if the password is true or false(Boolean)
#Meaning that if I just write "Joe" and the code has if length <=6, >3, etc.
#It wouldn't know long "Joe" is without lentgh 