# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 05:30:52 2022

@author: Joseph Bonadeo
"""

for number in range(3):
        print("successful")

print("\n")        

for number in range(3):
        print("successful", number +1)

print("\n")
        
     
for number in range(3):
        print("successful", number +1, (number+1) * ".")

print("\n")   

for number in range(1,4):
    print("successful", number, (number+1) * ".")
    
print("\n")   

for number in range(1,10,2):
    print("successful", number, (number+1) * ".")    
 
print("\n") 

    
successful=True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break


print("\n") 
    
successful=False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
    
print("\n")

print("Nested Loop")    
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")
      
print("\n")  
      
##Range is iterable
##string is iterable

for x in "INFO-233":
    print(x)

print("\n")

# lists are iterable

for x in [1,2,3,4]:
    print(x)
    
print("\n")
    
for number in range(1,10):
    if number %2 == 0:
        print(number)
      
print("\n")
        
count = 0        
for number in range(1,10):
    if number %2 == 0:
        count +=1
        print(number)        
print (f"We have {count} even numbers")


print("\n")


i=0
while i <= 10:
    print(i)
    i+=1

print("loop done")

print("\n")

i=0
list1=["tree","branch","trunk","bark", "leaf"]
while i < len(list1):
    print(list1[i])
    i+=1
  
print("\n")
    
#Helpful to remeber
num = 4
print(f"my number is {num} not 5")

#more you unique way to do it

print("\n")

num = input('What number would you like? ')
print(f"my number is {num} not 5")

