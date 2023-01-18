##Repeat with while

count = 1
while count <= 5:
    print(count)
    count += 1
    
##Cancel with break
#If you want to loop until something occurs, but you’re not sure when that
#might happen, you can use an infinite loop with a break statement. This
#time, let’s read a line of input from the keyboard via Python’s input()
#function and then print it with the first letter capitalized. We break out of the
#loop when a line containing only the letter q is typed:
    
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
    
##Skip Ahead with continue
#Sometimes, you don’t want to break out of a loop but just want to skip
#ahead to the next iteration for some reason. Here’s a contrived example:
#let’s read an integer, print its square if it’s odd, and skip it if it’s even. We
#even added a few comments. Again, we use q to stop the loop:


while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q': # quit
        break
    number = int(value)
    if number % 2 == 0: # an even number
        continue
    print(number, "squared is", number*number)
    
##Check break Use with else

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
        position += 1
    else: # break not called
        print('No even number found')
        
##Iterate with for and in

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
offset += 1

#But there’s a better, more Pythonic way:
    
for letter in word:
    print(letter)

##Cancel with break

word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)
    
##Skip with continue
#Inserting a continue in a for loop jumps to the next iteration of the loop,
#as it does for a while loop.

##Check break Use with else

word = 'thud'
for letter in word:
    if letter == 'x':
        print("Eek! An 'x'!")
    break
    print(letter)
else:
    print("No 'x' in there.")
    
#Generate Number Sequences with range()

for x in range(0,3):
    print(x)
#or

list( range(0, 3) )

#Here’s how to make a range from 2 down to 0:

for x in range(2, -1, -1):
    print(x)
#or

list( range(2, -1, -1) )

#The following snippet uses a step size of 2 to get the even numbers from 0 to 10:

list( range(0, 11, 2) )