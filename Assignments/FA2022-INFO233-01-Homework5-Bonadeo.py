# Course: Introduction to Programming (INFO-233)
# Student Name: Joseph Bonadeo  

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

##############
# Problem 1
##############

# Combining what we learned
# we've learned a lot over the last few weeks. Let's put that to use
# Create a code block which consists of a function to average grades and a function to assign a letter grade
# to the average returned by your function

#The average function should be able to take any number of grades
# Use two for loops to calculate the average of the grades and return it to the main program. One loop calculates
# how many grades are to be averaged and the second sums the grades. 
# use the function you previously creeated to assign a letter grade to the average by passing the 
# returned average to your letter grade function and print out the number grade to two deciamal places and the letter grade
#Use 100.100.70.60 as the input to the function

##HINT, you tested for grades before, right, reuse the code.  Code resuse is one of the best ways to 
#things done quickly
""" Expected Output

Your average is 82.5
Your final grade is B
"""

##############
# Problem 1 code goes below
##############

def testAvg(exam_list):
    total = 0 
    for j in exam_list:
        total += j

    average = total/len(exam_list)
    return average

def overallGrade(test_average):        
    if test_average >= 90:
     return("A")
    elif test_average >= 80:
     return("B")
    elif test_average >= 70:   #used reutrn and not print instead. Allowed me to display grade 
     return("C")
    elif test_average >= 60:
     return("D")
    else:
     return("F")
 
 
exam_list = []

while(True):
    scores = input('Enter your test scores and press "p" to show final grade: ') #adding p to allow the code to know when to stop while inputing your grades
#Also if I dont add "p" it will keeping asking the same question over and over
    
    if scores == "p":
        break
    exam_list.append(float(scores))

test_average = testAvg(exam_list)
overallGrade = overallGrade(test_average)

print('Your average grade is %.2f\nYour final grade is %s' %(test_average, overallGrade))

##############
# Problem 2
##############

#Now that you get how to use a function , pass argumanets and return values, copy the code from above
# modify it so it takes input from a user, The input should be comma separated (each grade is separated by a comma)
# 
##HINT Remember, an input is always type string. You will have to convert the string input
# to a list of floats. Modify your averages function and replace the second for loop with the sum() function 
# to get the total of all of the grades. 


"""Expected Outout

Please enter grades separated by a comma (,)100,98.5,99.5,65.3,78.2,32.2,65
Your average is 76.96
Your final grade is C

"""
##############
# Problem 2 code goes below
##############


def testAvg(exam_list):
  return sum(exam_list)/len(exam_list)


def overallGrade(test_average):        
    
    if test_average >= 90:
     return("A")
    elif test_average >= 80:
     return("B")
    elif test_average >= 70:   #used reutrn and not print instead. Allowed me to display grade 
     return("C")
    elif test_average >= 60:
     return("D")
    else:
     return("F")


scores = input('Please enter grades separated by a comma (,):') 
exam_liststr = scores.split(",")
exam_list = [float(x) for x in exam_liststr]

test_average = testAvg(exam_list)
overallGrade = overallGrade(test_average)

print('Your average grade is %.2f\nYour final grade is %s' %(test_average, overallGrade))

