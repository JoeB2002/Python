from bs4 import BeautifulSoup
import requests

URL= "https://www.ramapo.edu/asb/"  #My url
headers = {"Content-Type":"application/json", "User-agent":"Mozilla"} # Add Http headers
page = requests.get(URL) # My web page

print(page)
print (type(page))
print(page.text)

print('\n')###################################################################

soup = BeautifulSoup(page.content, "html.parser") # soupify the webpage
tags= soup.find(id="row-courses") # find tags with the id text. 
print(tags)

print('\n')####################################################################

print(tags.prettify())

print('\n')####################################################################

academic_program =tags.find("h3") # finds the first tag
print(academic_program)
print (type(academic_program))

print('\n')####################################################################

for tag in tags:
        academic = tag.find('h3').text
        try:
            degree = tag.find('h4').text
               
        except AttributeError:
            degree = "None"
            
        myList = [academic, degree]
        print(myList)
        
print('\n')####################################################################

academics =[] # create an empty list
academic_programs = tags.find_all("h3") # now use the tags found to find the <h3>. This returns a BS4 result set
for tag in academic_programs: #iterate through the tags
   academics.append(tag.text) # append the tag's text into the list
print(type(academics)) # check to see our list is indeed a list
print (academics) 

print('\n')####################################################################

myTuple= tuple(academics) #convert the list to a tuple
print (type(myTuple)) # check to see the new tuple is indeed a tuple
print(myTuple)

print('\n')####################################################################

degree_tags =tags.find_all("h4")
print(degree_tags)

print('\n')####################################################################

degrees=[]
for tag in degree_tags: #iterate through the tags
   degrees.append(tag.text) # append the tag's text into the list
print(type(degrees)) # check to see our list is indeed a list
print (degrees) 

print('\n')####################################################################

print(f"The number of academic programs offered by the Ansfield School of Business is {len(myTuple)}")

print('\n')####################################################################

from csv import writer
import csv

#Use with open to automatically keep the file open and close it after the loop
with open('ASB Academic Programs.csv', 'w', encoding='utf8', newline='') as f: 
    thewriter = writer(f) # create a writer object.
    header=['Academic Program','Degree Program'] # column headers in CSV
    thewriter.writerow(header) # write the column headings first

        
    for tag in tags:
        try: # try as a null will cause an Attribute error
           academic = tag.find('h3').text # find all the h3 tags again

        except AttributeError:
            academic = "None"

        try:# try as a null will cause an Attribute error
           degree = tag.find('h4').text # find all the h4 tags again

        except AttributeError:
            degree = "None"
        myList = [academic, degree]
        thewriter.writerow(myList)
        print (myList)                       
        
print('\n')####################################################################

with open("ASB Academic Programs.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      print(row)
      
