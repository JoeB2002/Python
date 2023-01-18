favFruits = ['apple', 'banana', 'peach', 'pear', 'pineapple', 'orange', 'grape', 'plum']
fruit= 0
while fruit <(len(favFruits)):
    print(favFruits[-fruit-1])
    fruit +=1

print('\n')
    
aString=('The weather today is cloudy with a chance of rain at 80%')
print(aString[4:17])

print('\n')

for i in range (10,15,1):
    print(i, end=',')
    
print('\n')

def subNumbers(a, b):
     return (a-b)
 
# main code
a = 90
b = 50
 
# finding subtraction
result = subNumbers(a, b)
 
# print statement
print("subtraction of ", a, " and ", b, " is = ", result)

print('\n')

import math
  
# function to check if prime or not 
def check(n):
    if n == 1:
        return False
          
        # from 1 to sqrt(n) 
    for x in range(2, (int)(math.sqrt(n))+1):
        if n % x == 0:
            return False 
    return True
  
# driver code
n = 23
if check(n):
    print("prime") 
else:
    print("not prime")
    
print('\n')
    
def meow(joe):
        return joe*joe+joe

result = meow(23)
print(result)

print('\n')

print(f'Number\t\tSquare\t\tCube')
for x in range(1, 11):
 print(f'{x:2d}\t\t\t{x*x:3d}\t\t\t{x*x*x:4d}')
 
print('\n')

## F-strings

first_name = 'Joe'
last_name = 'Bonadeo'
string1 = 'Hello my name is Joe Bonadeo'

string3 = f'Hello my name is {first_name} {last_name}'
print(string3)

print('\n')

string4 = f'Hello my name is {first_name} {last_name.upper()}'
print(string4)

print('\n')

def larger (new):
    new = new.upper()
    return(new)

string5 = f'Hello my name is {first_name} {larger(last_name)}'
print(string5)
    
print('\n')

file_name = 'file'

for i in range(101):
    print (f'{file_name}_{i:03}')
    
print('\n')

from math import pi
for i in range(1,7):
    print (i)
    
print('\n')

from math import pi
for i in range(1,7):
    print (f'{pi:.{i}f}')