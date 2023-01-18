##Define a Function with def

#To define a Python function, you type def, the function name, parentheses
#enclosing any input parameters to the function, and then finally, a colon (:).
#Function names have the same rules as variable names (they must start with
#a letter or _ and contain only letters, numbers, or _).
#Let’s take things one step at a time, and first define and call a function that
#has no parameters. Here’s the simplest Python function:
    
def do_nothing():
    pass

#Even for a function with no parameters like this one, you still need the
#parentheses and the colon in its definition. The next line needs to be
#indented, just as you would indent code under an if statement. Python
#requires the pass statement to show that this function does nothing. It’s the
#equivalent of This page intentionally left blank (even though it isn’t
#anymore).

##Call a Function with Parentheses

def make_a_sound():
    print('quack')

make_a_sound()

print("\n") 

def agree():
    return True

print("\n") 

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')
    
##Arguments and Parameters
#At this point, it’s time to put something between those parentheses. Let’s
#define the function echo() with one parameter called anything. It uses the
#return statement to send the value of anything back to its caller twice,
#with a space between:
    
print("\n")

def echo(anything):
    return anything + ' ' + anything

print (echo('Rumplestiltskin'))

print("\n")

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."
    
#Call the function commentary() with the string argument 'blue'.

comment = commentary('blue')

#The function does the following:
#Assigns the value 'blue' to the function’s internal color parameter
#Runs through the if-elif-else logic chain
#Returns a string
#The caller then assigns the string to the variable comment.
#What did we get back?

print(comment)

# or 

print("\n")

print(do_nothing())

##None Is Useful

print("\n")

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

#To distinguish None from a boolean False value, use Python’s is operator:
    
print("\n")


thing = None
if thing is None:
    print("It's nothing")
else:
    print("It's something")
    
print("\n")
    

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")

whatis(None)

whatis(True)

whatis(False)

print("\n")

#How about some real values?

whatis(0)

whatis(0.0)

whatis('')

whatis("")

whatis('''''')

whatis(())

whatis([])

whatis({})

whatis(set())

whatis(0.00001)

whatis([0])

whatis([''])

whatis(' ')

##Positional Arguments
#Python handles function arguments in a manner that’s very flexible, when
#compared to many languages. The most familiar types of arguments are
#positional arguments, whose values are copied to their corresponding
#parameters in order.

#This function builds a dictionary from its positional input arguments and
#returns it:
    
print("\n")

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
menu('chardonnay', 'chicken', 'cake')

menu('beef', 'bagel', 'bordeaux')

##Keyword Arguments

print("\n")

menu(entree='beef', dessert='bagel', wine='bordeaux')

#or

menu('frontenac', dessert='flan', entree='fish')

##Specify Default Parameter Values

print("\n")


def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')

#or

menu('dunkelfelder', 'duck', 'doughnut')

print("\n")

def buggy(arg, result=[]):
    result.append(arg)
print(result)

buggy('a')

buggy('b') # expect ['b']

print("\n")

def works(arg):
    result = []
result.append(arg)
return result

works('a')

works('b')

print("\n")

def nonbuggy(arg, result=None):
    if result is None:
        result = []
result.append(arg)
print(result)

nonbuggy('a')

nonbuggy('b')

##Explode/Gather Positional Arguments with *

print("\n")

def print_args(*args):
    print('Positional tuple:', args)

print("\n")

print_args(3, 2, 1, 'wait!', 'uh...')

print("\n")

def print_more(required1, required2, *args):
    print('Need this one:', required1)
print('Need this one too:', required2)
print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print("\n")

print_args(2, 5, 7, 'x')

args = (2,5,7,'x')
print_args(args)

print_args(*args)

print("\n")

##Explode/Gather Keyword Arguments with **

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)

print_kwargs()

print("\n")

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

##Keyword-Only Arguments

print("\n")

def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)

print("\n")

print_data(data, start=4)

print("\n")

print_data(data, end=2)

print("\n")

##Mutable and Immutable Argument

outside = ['one', 'fine', 'day']
def mangle(arg):
    3
arg[1] = 'terrible!'

outside
['one', 'fine', 'day']
mangle(outside)
outside
['one', 'terrible!', 'day']

print("\n")

##Docstrings

def echo(anything):
    'echo returns its input argument'
return anything

print("\n")

def print_if_true(thing, check):
    '''
Prints the first argument if a second argument is true.
The operation is:
1. Check whether the *second* argument is true.
2. If it is, print the *first* argument.
'''
if check:
    print(thing)

print("\n")

help(echo)

print("\n")

print(echo.__doc__)

print("\n")

##Functions Are First-Class Citizens

def answer():
    print(42)

print("\n")

answer()

def run_something(func):
    func()

run_something(answer)

print("\n")

type(run_something)

print("\n")

def add_args(arg1, arg2):
    print(arg1 + arg2)

print("\n")

type(add_args)

print("\n")

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

print("\n")

run_something_with_args(add_args, 5, 9)

print("\n")

def sum_args(*args):
     sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

run_with_positional_args(sum_args, 1, 2, 3, 4)

print("\n")

##Inner Functions

def outer(a, b):
    def inner(c, d):
        return c + d
return inner(a, b)

outer(4, 7)

print("\n")

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
return inner(saying)

knights('Ni!')

##Closures

print("\n")

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')

print("\n")

type(a)

type(b)

print("\n")

a()

b()

print("\n")

##Anonymous Functions: lambda

def edit_story(words, func):
    for word in words:
        print(func(word))

print("\n")

stairs = ['thud', 'meow', 'thud', 'hiss']

print("\n")

def enliven(word): # give that prose more punch
    return word.capitalize() + '!'

print("\n")

edit_story(stairs, enliven)

print("\n")

edit_story(stairs, lambda word: word.capitalize() + '!')


##Generators

sum(range(1, 101))


##Generator Functions

print("\n")

def my_range(first=0, last=10, step=1):
    number = first
while number < last:
    yield number
number += step

my_range

print("\n")

ranger = my_range(1, 5)
ranger

print("\n")

for x in ranger:
    print(x)

print("\n")

for try_again in ranger:
    print(try_again)


##Generator Comprehensions

print("\n")

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
genobj

print("\n")

for thing in genobj:
    print(thing)


##Decorators
#A decorator is a function that takes one function as input and returns
#another function. Let’s dig into our bag of Python tricks and use the
#following:
#*args and **kwargs
#Inner functions
#Functions as arguments
#The function document_it() defines a decorator that will do the following:
#Print the function’s name and the values of its arguments
#Run the function with the arguments
#Print the result
#Return the modified function for use
#Here’s what the code looks like:

print("\n")

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
print('Positional arguments:', args)
print('Keyword arguments:', kwargs)
result = func(*args, **kwargs)
print('Result:', result)
return result
return new_function

print("\n")

def add_ints(a, b):
    return a + b

add_ints(3, 5)

print("\n")

cooler_add_ints = document_it(add_ints) # manual decorator assignment
cooler_add_ints(3, 5)

@document_it
def add_ints(a, b):
    return a + b

print("\n")

add_ints(3, 5)

print("\n")

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
return result * result
return new_function

print("\n")

@document_it
@square_it
def add_ints(a, b):
    return a + b

print("\n")

add_ints(3, 5)

print("\n")

@square_it
@document_it
def add_ints(a, b):
    return a + b

print("\n")

add_ints(3, 5)

##Namespaces and Scope

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)

print("\n")

print_global()

print("\n")

#But if you try to get the value of the global variable and change it within the
#function, you get an error:
    
#>>> def change_and_print_global():
#... print('inside change_and_print_global:', animal)
#... animal = 'wombat'
#... print('after the change:', animal)
#...
#>>> change_and_print_global()
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#File "<stdin>", line 2, in change_and_print_global
#UnboundLocalError: local variable 'animal' referenced before assignment
#If you just change it, it changes a different variable also named animal, but
#this variable is inside the function:
    
print("\n")

def change_local():
    animal = 'wombat'
print('inside change_local:', animal, id(animal))

change_local()

animal

id(animal)

print("\n")

animal = 'fruitbat'
def change_and_print_global():
    global animal
animal = 'wombat'
print('inside change_and_print_global:', animal)

print("\n")

animal

print("\n")

change_and_print_global()

print("\n")

animal

animal = 'fruitbat'
def change_local():
    animal = 'wombat' # local variable
print('locals:', locals())

print("\n")

animal


print("\n")

change_local()
locals: {'animal': 'wombat'}
print('globals:', globals()) # reformatted a little for presentation
globals: {'animal': 'fruitbat',

print("\n")

##Uses of _ and __ in Names


#def amazing():
    #'''This is the amazing function.
   # Want to see it again?'''
    #print('This function is named:', amazing.__name__)
   #print('And its docstring is:', amazing.__doc__)

#amazing()


##Recursion

#def flatten(lol):
        #for item in lol:
            #if isinstance(item, list):
                #for subitem in flatten(item):
                    #yield subitem
           #else:
                #yield item

#lol = [1, 2, [3,4,5], [6,[7,8,9], []]]


#def flatten(lol):
#for item in lol:
#if isinstance(item, list):
#yield from flatten(item)
#else:
#yield item

#lol = [1, 2, [3,4,5], [6,[7,8,9], []]]
#list(flatten(lol))


##Exceptions


#short_list = [1, 2, 3]
#position = 5
#try:
#short_list[position]
#except:
#print('Need a position between 0 and', len(short_list)-1, ' but got',
#position)

#print("\n")

#short_list = [1, 2, 3]
#while True:
#value = input('Position [q to quit]? ')
#if value == 'q':
#break
#try:
#position = int(value)
#print(short_list[position])
#except IndexError as err:
#print('Bad index:', position)
#except Exception as other:
#print('Something else broke:', other)

#print("\n")

#try:
#raise OopsException('panic')
#except OopsException as exc:
#print(exc)