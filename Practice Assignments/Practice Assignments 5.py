def newline():
    print('\n')
#define our functions first

def do_nothing():
    print('nothing')

def shout():
    print("Shout out to the World!")

def square_It(inputnum):
    print(inputnum **2)
    
#don't name all variables the same thing

mynumber= int(input('enter a whole number' ))
square_It(mynumber)

###############################################################################

def square_It(inputnum):
    out_num= inputnum ** 2   # Do the math
    print(out_num)  # print the result
    return out_num # return the value stored in out_num back to the main program global variable my_new_num

print('\n')

in_num = (int(input("Enter a whole number "))) # get the input
my_new_num = square_It(in_num) # Call to the function passing the input number to the function and store it in my_new_num
print(" my_new_num is ", my_new_num) # print a statement and the result of the function

###############################################################################

def sumAll(*args):
    total = 0
    for arg in args:
        total += arg
    return total


x = sumAll(5, 4, 3, 2, 1)
print(x)

#local on mobile to the function 

#global is the whole entire code











