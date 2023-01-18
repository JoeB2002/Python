courses = ['Math', "English", "History", "Pyhsics"]

print(courses[2:])


print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

courses.append('Art')

print(courses)


print('\n')
###############################################################################

#If I want to put it in a specefic location

courses = ['Math', "English", "History", "Pyhsics"]

courses.insert(0, 'Art')

print(courses)


print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]
courses2 = ['Art', 'Education']

courses.extend(courses2)

print(courses)


print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

courses.pop()

print(courses)


print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

courses.reverse()

print(courses)


print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

for course in courses:
    print(course)

print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

for index, course in enumerate(courses):
    print(index, course)

print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

course_str = ', '.join(courses)

print(course_str)

print('\n')
###############################################################################

courses = ['Math', "English", "History", "Pyhsics"]

course_str = ', '.join(courses)

newList = course_str.split(' - ')

print(newList)


print('\n')
###############################################################################

#Mutable

list_1 = ['Math', "English", "History", "Pyhsics"]
list_2 = list_1

print(list_1)
print(list_2)

print('\n')

list_1[0] = 'Art'

print(list_1)
print(list_2)

print('\n')
###############################################################################

#Immutable

tuple_1 = ('Math', "English", "History", "Pyhsics")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

print('\n')

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

print('\n')
###############################################################################

myString = 'Welcome to INFO-233\'s midterm'
for i in myString:
    print(i)
    
print('\n')
###############################################################################

count = 0 
while (count < 3):
    count = count + 1
    print('Hello World')
else:
    print('The End')