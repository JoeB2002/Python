# Course: Introduction to Programming (INFO-233)
# Student Name: Joseph Bonadeo 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

##############
# Problem 1
##############

# Create a list of values from 0 to 300 (including 300) in incremenets of 3 (0, 3, 6...).
# Iterate through every value, and confirm whether the value is even or odd.
# Do you notice anything interesting?
##HINT Create an empty list. Research .append() method. Iterate through a range of numbers 
#as specified and append the values to the list. iterate through the new list and test each value 
# for odd and even
 
""" Expected Output
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78,
 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138, 141, 144,
 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198, 201, 204, 207,
 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 258, 261, 264, 267, 270,
 273, 276, 279, 282, 285, 288, 291, 294, 297, 300]

0 is even
3 is odd
6 is even
9 is odd
.
.
.
300 is even
"""
##############
# Problem 1 code goes below here
##############


list2 = list(range(0,301,3))
print(list2)

print("\n") 

list2 
empty_list=[] 
for i in list2: 
    if(i%2==0): #This is going to check if value is even or not
        empty_list.append(f'{i} is even') 
    else:
        empty_list.append(f'{i} is odd') 
        
print('\n'.join(empty_list))


##############
# Problem 2
##############
# Tuition increases are common. Our tuition is currently $8000 a year. 
#With an expected increase of 3% a year for the next 5 years, write code to calculate
# the tuition for each year for 5 consecutive years.  
#Write the code twice, once with for loop and once with a while loop

""" Expected Output
Tution will increase from the current amount of: $8,000.00 as follows: 

Year 	 New Tuition
---- 	 -----------
2023 	 $8,240.00
2024 	 $8,487.20
2025 	 $8,741.82
2026 	 $9,004.07
2027 	 $9,274.19
"""


##############
# Problem 2 code goes below here
##############

print("\n") 

tuition = 8000.00

print('Tuition will increase from the current amount of: $',format(tuition,',.2f') + ' as follows: ')

print("\n") 

tuition = 8000.00
print('Year\t New Tuition')
print('-' * 4 + '     -----------')
for year in range(2023, 2028):
    tuition += tuition * 0.03
    for h in range(1):
       print("%d\t ${:,.2f}".format(tuition) % (year))
       
print("\n") 

year = 2023
tuition = 8000
increase = 0.03
beg = 2023
end = 2028

print('Year\t New Tuition')
print('-' * 4 + '     -----------')
while year in range(beg, end):
    tuition = (tuition) + (tuition * increase)
    
    print("%d\t ${:,.2f}".format(tuition) % (year))
    year = year + 1  #This helps to end the code (don't go forever)

    
############
# Problem 3
##############

# Write code to display a table of Celsius temps from 0 to 20 and its Fahrenheit equivalent

# HINT## Use a loop and iterate through a range of numbers as specified above. Research how to add tabs in a print statement
#Research formatting to two decimal places with print. 
## formula to convert Farenheit to Celsius °F = (°C × 9/5) + 32
""" Expected Output
Celsius 	 Fahrenheit
------- 	 ----------
0 	 	 	 32.00
1 	 	 	 33.80
2 	 	 	 35.60
3 	 	 	 37.40
4 	 	 	 39.20
5 	 	 	 41.00
6 	 	 	 42.80
7 	 	 	 44.60
8 	 	 	 46.40
9 	 	 	 48.20
10 	 	 	 50.00
11 	 	 	 51.80
12 	 	 	 53.60
13 	 	 	 55.40
14 	 	 	 57.20
15 	 	 	 59.00
16 	 	 	 60.80
17 	 	 	 62.60
18 	 	 	 64.40
19 	 	 	 66.20
20 	 	 	 68.00
"""
##############
# Problem 3 code goes below here
##############

print("\n") 

start = 0
stop = 21
add_value= 1
print('')
print('Celsius\t      Fahrenheit')
print('-' * 7 + '       ----------')

for C in range (start, stop, add_value):
    F = (9 / 5) * C + 32
    print(C, '      \t', " {0:.2f}".format(F))






