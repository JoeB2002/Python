height = 5
if height > 4:
    print("You can ride")
else:
    print("Go home")
    
    # : is important ot add in if you dont have it, it wil freeze
    # Need to made it indented --> it will make it true 
    
print('\n')    
    
height = 6
if height == 5:
      print("You can ride")
elif height == 6:
    print("You are too tall")
else: print("Go home")

print('\n')    

height = input('What is your height? ')
str(height)
statement = "you are " + height
print(height)
print(statement)

print('\n')    

name = input("What is your name? ")
print("Hello " + name)

print('\n')    

print("A man", "A plan")

print('\n')    

print("A man \n A plan") #Don't really need to remeber this

print('\n') 
   
print("A quote from shakespeare, \'Oh Romeo\'")

print('\n')    

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[4])

print('\n')    

#If you want specific amount
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[1:4])

print('\n')    

#The 2 at the end; helps you move 2 over everytime
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[1:4:2])

print('\n')    

#The length of the string
letters = 'abcdefghijklmnopqrstuvwxyz'
print(len(letters))


