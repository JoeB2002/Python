furry = True
large = True
if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")


color = "mauve"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)
    

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
    
    
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
or letter == 'o' or letter == 'u':
    print(letter, 'is a vowel')
else:
    print(letter, 'is not a vowel')
    
    
vowels = 'aeiou'
letter = 'o'
letter in vowels

if letter in vowels:
    print(letter, 'is a vowel')


tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))


print("'There's the man that shot my paw!' cried the limping hound.")


print('Give', "us", '''some''', """space""")


poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''
print(poem)




palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

# By preceding a
#character with a backslash (\), you give it a special meaning. The most
#common escape sequence is \n, which means to begin a new line. With this
#you can create multiline strings from a one-line string:

    
testimony = "\"I did nothing!\" he said. \"Or that other thing.\""
testimony
print(testimony)

#You might also need \' or \" to specify a literal single or double quote
#inside a string that’s quoted by the same character:
    
    
fact = "The world's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)


poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
print(poem)

#or 

poem = r'''Boys and girls, come out to play.
The moon doth shine as bright as day.'''
poem
'Boys and girls, come out to play.\nThe moon doth shine as bright as day.'
print(poem)

#Combine by Using +

test = 'Release the kraken! ' + 'No, wait!'
print(test)


vowels = ( 'a'
"e" '''i'''
'o' """u"""
)
vowels
print(vowels)


a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c
'Duck.Duck.Grey Duck!'
print(a, b, c)

#Duplicate with *

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)


#Get a Character with []
    #To get a single character from a string, specify its offset inside square
    #brackets after the string’s name. The first (leftmost) offset is 0, the next is 1,
    #and so on. The last (rightmost) offset can be specified with –1, so you don’t
    #have to count; going to the left are –2, –3, and so on:
        
letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
'a'
letters[1]
'b'
letters[-1]
'z'
letters[-2]
'y'
letters[25]
'z'
letters[5]
'f'
print(letters)
#When putting 'letter' that is the answer 


name = 'Henny'
name.replace('H', 'P')
'Penny'
'P' + name[1:]
print(name)
#Can do either 


#Get a Substring with a Slice
    #[:] extracts the entire sequence from start to end.
    #[ start :] specifies from the start offset to the end.
    #[: end ] specifies from the beginning to the end offset minus 1.
    #[ start : end ] indicates from the start offset to the end offset
    #minus 1.
    #[ start : end : step ] extracts from the start offset to the end
    #offset minus 1, skipping characters by step.
    
    
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters)


#Get Length with len()

len(letters)
26
empty = ""
len(empty)


#Split with split()

tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
tasks.split(',')
print(tasks)

#or

tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
tasks.split()
print(tasks)


#Combine by Using join()

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)


#Substitute by Using replace()

setup = "a duck goes into a bar..."
setup.replace('duck', 'marmoset')
'a marmoset goes into a bar...'
print(setup)


#Strip with strip()

world = " earth "
world.strip()
'earth'
world.strip(' ')
'earth'
world.lstrip()
'earth '
world.rstrip()
' earth'
print(world)

blurt = "What the...!!?"
blurt.strip('.?!')
print(blurt)


#Search and Select

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''
print(poem)


#Still more to do but I have on anotherfile if I need help