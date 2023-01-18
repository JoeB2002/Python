#Tuples


empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho'
print(one_marx)

one_marx = ('Groucho',)
print(one_marx)

type(one_marx)
#Have to run seperatly 

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)

#or (don't really need them)

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

type(one_marx)
#Have to run seperatly

type('Groucho',)
#Have to run seperatly

type(('Groucho',))
#Have to run seperatly

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
print(a)
print(b)
print(c)

password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)
print(marx_list)

marx_list = ('Groucho',) + ('Chico', 'Harpo')
print(marx_list)

test =  ('yada',) * 3
print(test)

a = (7, 2)
b = (7, 2, 9)
a == b
print(a)
#should say false 
a <=b
print(a)
#should say True
a < b
print(a)
#should say True

words = ('fresh','out', 'of', 'ideas')
for word in words:
    print(word)
    
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop,')
#t1 + t2
#should come out to be: ('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop,')
#t1 += t2
#should come out to be: ('Fee', 'Fie', 'Foe', 'Flop')

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
#print(id(t1))
#should come out to be: 4365405712
#t1 += t2
##print(id(t1))
#should come out to be: 4364770744


#Lists

empty_list = [ ]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsatawney', {"groundhog": "Phil"}, "Feb. 2"]
another_empty_list = list()
print(another_empty_list)

word = ('cat')
mylist = list(word)
print(mylist)
#suppose to be: ['c', 'a', 't']

a_tuple = ('ready', 'fire', 'aim')
list = (a_tuple)
print(list)

#Split

talk_like_a_pirate_day = '9/19/2019'
talk_like_a_pirate_day.split('/')
print(talk_like_a_pirate_day.split('/'))

splitme = 'a/b//c/d///e'
splitme.split('/')
print(splitme.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
#or
print(marxes[1])
#or
print( marxes[-3])

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
#or
print(marxes[::2])
#or
print(marxes[::-2])
#or
print(marxes[::-1])

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
#or
print(marxes[-6:])
#or
print(marxes[-6:-2])
#or
print(marxes[-6:-4])

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
#or
marxes.insert(10, 'Zeppo')
print(marxes)

test = ["blah"] * 3
print(test)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100)
print( numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(marxes[-1])
#or
del marxes[-1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo']
del marxes[1]
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.remove('Groucho')
print(marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
#or
print(marxes)
#or
print(marxes.pop(1))
#or
print(marxes)

work_quotes = ['Working hard?', 'Quick question!', 'Number one priorities!']
print(work_quotes)
#or
work_quotes.clear()
print(work_quotes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
print(simpsons.index('Bart'))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
#or
print('Bob' in marxes)

words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
#or
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))

friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
#or
separated = joined.split(separator)
print(separated)
#or
print(separated == friends)

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
print(sorted_marxes)

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
#But now when you add list function
marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print( numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))

a = [1, 2, 3]
print(a)
#or
b = a
print(b)
#or
a[0] = 'surprise'
print(a)
#So now with b
print(b)
#or
b[0] = 'I hate surprises'
print(b)
#or
print(a)

a[0] = 'integer lists are boring'
print(a)
#or
#print(b)
#which should be [1, 2, 3]
#or
#print(c)
#which should be [1, 2, 3]
#or
#print(d)
#which should be [1, 2, 3]

a = [1, 2, [8, 9]]
b = a.copy()
d = a[:]
print(a)
#or
print(b)
#or
#print(c)
#which should be [1, 2, [8, 9]]
#or
print(d)

a[2][1] = 10
print(a)
#or
print(b)
#or
#print(c)
#which should be [1, 2, [8, 10]]
#or
print(d)

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(a)
#or
print(b)
#or
a[2][1] = 10
print(a)
#or
print(b)

a = [7, 2]
b = [7, 2, 9]
print(a == b)
#or
print(a <= b)
#or
print(a < b)

cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
    
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
        
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # no break means no cheese
    print('This is not much of a cheese shop, is it?')

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
    
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
#list( zip(english, french) )
#should be [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
##or
#dict( zip(english, french) )
#{'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)
#or
#number_list = list(range(1, 6))
#print(number_list)
#should say [1, 2, 3, 4, 5]

number_list = [number for number in range(1,6)]
#print(number_list)
#should say [1, 2, 3, 4, 5]

number_list = [number-1 for number in range(1,6)]
#print(number_list)
#shoudl say [0, 1, 2, 3, 4]

a_list = [number for number in range(1,6) if number % 2 == 1]
#print(a_list)
#[1, 3, 5]

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

#print(a_list)
#should be [1, 3, 5]

rows = range(1,4)
cols = range(1,3)
#for row in rows:
    #for col in cols:
        #print(row, col)
#should be 
#1 1
#1 2
#2 1
#2 2
#3 1
#3 2

rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
    
for row, col in cells:
    print(row, col)
    
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
#or
print(all_birds[0])
#or
print(all_birds[1])
#or
print(all_birds[1][0])


#Tuples Versus Lists

#You can often use tuples in place of lists, but they have many fewer
#functions—there is no append(), insert(), and so on—because they can’t
#be modified after creation. Why not just use lists instead of tuples
#everywhere?
#Tuples use less space.
#You can’t clobber tuple items by mistake.
#You can use tuples as dictionary keys (see Chapter 8).
#Named tuples (see “Named Tuples”) can be a simple alternative to
#objects.
#I won’t go into much more detail about tuples here. In everyday
#programming, you’ll use lists and dictionaries more.


#There Are No Tuple Comprehensions

#Mutable types (lists, dictionaries, and sets) have comprehensions.
#Immutable types like strings and tuples need to be created with the other
#methods listed in their sections.
#You might have thought that changing the square brackets of a list
#comprehension to parentheses would create a tuple comprehension. And it
#would appear to work because there’s no exception if you type this:
#>>> number_thing = (number for number in range(1, 6))
#The thing between the parentheses is something else entirely: a generator
#comprehension, and it returns a generator object:
#>>> type(number_thing)
#<class 'generator'>
#I’ll get into generators in more detail in “Generators”. A generator is one
#way to provide data to an iterator.

###############################################################################
#Dictionaries

#A dictionary is similar to a list, but the order of items doesn’t matter, and
#they aren’t selected by an offset such as 0 or 1. Instead, you specify a
#unique key to associate with each value. This key is often a string, but it can
#actually be any of Python’s immutable types: boolean, integer, float, tuple,
#string, and others that you’ll see in later chapters. Dictionaries are mutable,
#so you can add, delete, and change their key-value elements. If you’ve
#worked with languages that support only arrays or lists, you’ll love
#dictionaries.


empty_dict = {}
print( empty_dict)

bierce = {
"day": "A period of twenty-four hours, mostly misspent",
"positive": "Mistaken at the top of one's voice",
"misfortune": "The kind of fortune that never misses",
}
print (bierce)

acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)

acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

##One limitation of the second way is that the argument names need to belegal 
#variable names (no spaces, no reserved words):
#>>> x = dict(name="Elmer", def="hunter")
#File "<stdin>", line 1
#x = dict(name="Elmer", def="hunter")
#^
#SyntaxError: invalid syntax

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol))

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(tol))

los = [ 'ab', 'cd', 'ef' ]
print(dict(los))

tos = ( 'ab', 'cd', 'ef' )
(dict(tos))

pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
}
print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons)

some_pythons = {
'Graham': 'Chapman',
'John': 'Cleese',
'Eric': 'Idle',
'Terry': 'Gilliam',
'Michael': 'Palin',
'Terry': 'Jones',
}
print(some_pythons)

#This is the most common use of a dictionary. You specify the dictionary and
#key to get the corresponding value: Using some_pythons from the previous
#section:
#>>> some_pythons['John']
#'Cleese'
#If the key is not present in the dictionary, you’ll get an exception:
#>>> some_pythons['Groucho']
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#KeyError: 'Groucho'
#There are two good ways to avoid this. The first is to test for the key at the
#outset by using in, as you saw in the previous section:
#>>> 'Groucho' in some_pythons
#False
#3The second is to use the special dictionary get() function. You provide the
#dictionary, key, and an optional value. If the key exists, you get its value:
#>>> some_pythons.get('John')
#'Cleese'
#If not, you get the optional value, if you specified one:
#>>> some_pythons.get('Groucho', 'Not a Python')
#'Not a Python'
#Otherwise, you get None (which displays nothing in the interactive
#interpreter):
#>>> some_pythons.get('Groucho')
#>>>

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
##or
#list(signals.keys())
#should be ['green', 'yellow', 'red']
##or
#list( signals.values() )
###Get All Values with values()
#should be ['go', 'go faster', 'smile for the camera']
##or
###Get All Key-Value Pairs with items()
#list( signals.items() )
#should be [('green', 'go'), ('yellow', 'go faster'), ('red', 'smile for the camera')]
##or 
###Get Length with len()
#len(signals)
#should be 3

first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
print({**first, **second})

third = {'d': 'donuts'}
print({**first, **third, **second})

pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Gilliam': 'Terry',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
}
print(pythons)
#or
pythons = {
'Chapman': 'Graham',
'Cleese': 'John',
'Gilliam': 'Terry',
'Idle': 'Eric',
'Jones': 'Terry',
'Palin': 'Michael',
}
others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)
############################
del pythons['Marx']
print(pythons)
#or
del pythons['Howard']
print(pythons)

print(len(pythons))

print(pythons.pop('Palin'))

#print(pythons.pop('Palin'))
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#KeyError: 'Palin'
##This combines get() and del. If you give pop() a key and it exists in the
#dictionary, it returns the matching value and deletes the key-value pair. If it
#doesn’t exist, it raises an exception:
    
print(pythons.pop('First', 'Hugo'))
print(len(pythons))

pythons.clear()
print(pythons)

pythons = {}
print(pythons)

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
#or
print('Palin' in pythons)
#or
print('Gilliam' in pythons)

signals = {'green': 'go',
'yellow': 'go faster',
'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

signals = {'green': 'go',
'yellow': 'go faster',
'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
#or
print(original_signals)

signals = {'green': 'go',
'yellow': 'go faster',
'red': ['stop', 'smile']}
signals_copy = signals.copy()
print(signals)
#or
print(signals_copy)

signals['red'][1] = 'sweat'
print(signals)
#or
print(signals_copy)

import copy
signals = {'green': 'go',
'yellow': 'go faster',
'red': ['stop', 'smile']}
signals_copy = copy.deepcopy(signals)
print(signals)
#or
print(signals_copy)
#or
signals['red'][1] = 'sweat'
print(signals)
#or
print(signals_copy)

a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)

##Not to do 
#a = {1:1, 2:2, 3:3}
#b = {3:3, 1:1, 2:2}
#print(a <= b)
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: '<=' not supported between instances of 'dict' and 'dict'

a = {1: [1, 2], 2: [1], 3:[1]}
b = {1: [1, 1], 2: [1], 3:[1]}
print(a == b)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
'person': 'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)
#or
for value in accusation.values():
    print(value)
#or
for item in accusation.items():
    print(item)
#or
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
    
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word)
if letter in vowels}
print(vowel_counts)

#Sets

empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)

odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

set( 'letters' )
#should say {'l', 'r', 's', 't', 'e'}


set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
#should say {'Dancer', 'Dasher', 'Mason-Dixon', 'Prancer'}

set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
#should say set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )

set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} )
#should say {'cherry', 'orange', 'apple'}

reindeer = set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
print(len(reindeer))

s = set((1,2,3))
print(s)

s.add(4)
print(s)

s = set((1,2,3))
s.remove(3)
print(s)

furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

drinks = {
'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'},
'white russian': {'cream', 'kahlua', 'vodka'},
'manhattan': {'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
#or
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
        'cream' in contents):
            print(name)

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
       print(name)
       
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

print(a & b)
#or
print(a.intersection(b))
#or
print(bruss & wruss)
#or
print(a | b)
#or
print(a.union(b))
#or
print(bruss | wruss)

print(a - b)
#or
print(a.difference(b))
#or
print(bruss - wruss)
#or
print(wruss - bruss)

print(a ^ b)
#or
print(a.symmetric_difference(b))

print(bruss ^ wruss)

print(a <= b)
#or
print(a.issubset(b))

print(bruss <= wruss)
#or
print(a <= a)
#or
print(a.issubset(a))

print(a < b)
#or
print(a < a)
#or
print(bruss < wruss)

print(a >= b)
#or
print(a.issuperset(b))
##A superset is the opposite of a subset (all members of the second set are
#also members of the first). This uses >= or issuperset():

print(a > b)
#or
print(wruss > bruss)
##And finally, you can find a proper superset (the first set has all members of
#the second, and more) by using >, as shown here:
    
print(a > a)

a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

print(frozenset([3, 2, 1]))
#or
print(frozenset(set([2, 1, 3])))
#or
print(frozenset({3, 1, 2}))
#or
print(frozenset( (2, 3, 1) ))

fs = frozenset([3, 2, 1])
print(fs)
#or
#NOT TO DO
#fs.add(4)
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#AttributeError: 'frozenset' object has no attribute 'add'


#Data Structures So Far

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(marx_list[2])
#or
print(marx_tuple[2])
#or
print(marx_dict['Harpo'])
#or
print('Harpo' in marx_list)
#or
print('Harpo' in marx_tuple)
#or
print('Harpo' in marx_dict)
#or
print('Harpo' in marx_set)


#Make Bigger Data Structures

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
#or
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

houses = {
(44.79, -93.14, 285): 'My House',
(38.89, -77.03, 13): 'The White House'
}
print(houses)