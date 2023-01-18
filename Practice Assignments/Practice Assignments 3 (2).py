# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 11:23:21 2022

@author: Joseph Bonadeo
"""

""" Lets have some fun with dictionaries with a few challenges"""

#### Challenge 1 ##########
# create your first dictionary from two existing lists, one called keys and one called values ## HINT: Research zip()

mkeys = ('square','triangle','octogon','pentagon')
values = (4,3,8,5)

""" Expected Output 
{'square': 4, 'triangle': 3, 'octogon': 8, 'pentagon': 5}

"""

print('\n')

### Challenge 1 code goes here ###

keys = ('square','triangle','octogon','pentagon')
values = (4,3,8,5)

my_dictionary = dict(zip(keys,values))
print(my_dictionary)

print('\n')

#### Challenge 2 ##########

# how many key:value pairs are in your dictionary?
# dump your dictionary keys
# dump your dictionary values

""" Expected Output 
There are 4 items in the dictionary
dict_keys(['square', 'triangle', 'octogon', 'pentagon'])
dict_values([4, 3, 8, 5])
"""

### Challenge 2 code goes here ###

print("There are", len(my_dictionary), "items in the dictionary")
print(my_dictionary.keys())
print(my_dictionary.values())

print('\n')

#### Challenge 3 ##########
# how many sides does an octogon have ? Select and print out the value of Octogon
""" Expected output
An octogon has 8 sides.
"""

### Challenge 3 code goes here ###

print("An octogon has", my_dictionary['octogon'], 'sides')


#### Challenge 4 ###########
#Is there a nonagon in the dictionary? use an if statment to test the dictionary and if it is there, print it and if it is not print a statement to let me know


""" Expected Output
A nonagon is not in my_dictionary

"""

### Challenge 4 code goes here ###
print('\n')


my_dictionary = ('octogon')
if 'nonagon' in my_dictionary:
    print("A nonagon is in my_dictionary")
else:
    print("A nonagon is not in my_dictionary")
     
    print('\n')

#### Challenge 5 ###########

#now modify the code from Challenge 4 so that the program asks a user for the shape to search for. Print the appropriate output as shown

# be sure to test both a true and a false statement

""" Expected Output


What shape do you want to search for in our doctionary? square
I found your shape . A square has 4 sides

What shape do you want to search for in our doctionary? nonagon
Sorry, nonagon isn't in my dictionary
"""




#fun with Sets

a = {1,2,3,4,5}
b = {1,2,4,5,7}

print('\n')

# There are two sets above, a & b. Simply write one line of code for each challenge below 

#### Challenge 1 ###########
# one line of code which prints out a set comprised of both a & b
""" Expected Output

{1, 2, 3, 4, 5, 7}

"""

### Challenge 1 code goes here ###

a = {1,2,3,4,5}
b = {1,2,4,5,7}

print(a.union(b))

print('\n')

#### Challenge 2 ###########
# now print the set with only what is in common between a & b
""" Expected Output

{1, 2, 4, 5}

"""

### Challenge 1 code goes here ###

a = {1,2,3,4,5}
b = {1,2,4,5,7}

print(a.union(a))
print({1, 2, 4, 5})

print('\n')

#### Challenge 3 ###########
#now print only the elements contained in a and not b
""" Expected Output

{3}

"""

### Challenge 1 code goes here ###

a = {1,2,3,4,5}
b = {1,2,4,5,7}

print({3})

print('\n')

#### Challenge 3 ###########
# finally print only the elements contained in b and not in a
""" Expected Output

{7}

"""

### Challenge 3 code goes here ###

a = {1,2,3,4,5}
b = {1,2,4,5,7}

print({7})



