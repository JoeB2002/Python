# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:42:03 2022

@author: Joseph Bonadeo 
"""
## Country code List
## https://www.iban.com/country-codes
## https://openweathermap.org/current

""" For this assignment you are going to explore a weather API. Part 1 of the code is due in class.  Part 2 will be the homework for
the week.

We are building a program to get the current weather using an API. The openweather api contains all types of weather related items. 
For this exercise we will use the current weather data API
The documentatiuon can be found:

https://openweathermap.org/current



Ther are a couple of prerequisites to use openweathermap's API. 

1.  We must obtain an API key in order to authenticate to this API
2. This weather call will require you to get the longitude and latitude of a city and pass it to the weather API.  Since a city name is
not very precise as many different states can have a city with a common name (for example there are 14 separate citys in the US named
Dallas), our programs may not run perfectly if we just enter a city name to request the weather. A more accurate way in the US is to 
use a zipcode as zipcodes are unique for each city (i.e Dallas TX, 75001, Dallas CO, 75342) Fortunately for us, openweathermap has
an API to help us. It is the geocoding API 

https://openweathermap.org/api/geocoding-api

"""

## Part one of this assignment

## Prerequisites
## 1.  Register for an account at openweathermap.org. 
## 2.  Go to your email and confirm your account. Your API key won't be active until you do so
## 3.  Once you are logged in, you will see a tab API keys, click on it and retrieve your API Key.

## Part 1 consists of using the Geocoding API to return the longitude and latitude of a city
## Review the documentation of the Geocoding API
##  https://openweathermap.org/api/geocoding-api

## Create a program which
## 1. asks a user to input a zipcode
## 2. Pass the zipcode to the function get_zip and store the results in a tuple called lat_lon
## 3. Print the tuple to produce the output as shown in the expected output section. 


## Function definition
## 1. define a function called get_zip which
##  a. accepts the variable for zipcode from the main part of the program
##  b. calls results module with the URL for geocode
##  c. returns city, longitude , latitude to the main program
###
  
## hint ###
## use an input() to request the zip code and store it to a variable
## call your function passing the zip code to it and store it to a variable


## In the function, Review the recap section of the class notes. 
## store your API key in a variable
## include a variable for country_code and set it to 'US'
## store the URL for the API call to a variable called myURL -- Use fstring notation without the print and insert
## your variables in the appropriate places in the URL.  myURL = f"http://api.openweathermap.org........"
## Find the URL syntax in the documentation for the geocode API in the section titled Coordinates by zip/post code
## Call the api by passing your URL to the requests.get() method assigned to a variable named results
## create a variable which contains the results of your api call's json by assigning results.json() to the variable. 
## assign the lat, lon and city each to a variable and return them to the main program
## optionally print out the json using pprint to explore what is returned. 

""" Expected Output


Please enter a zipcode: 07430
The call returned code 200
The city name for 07430 is Mahwah
The latitude for 07430 is 41.0817
The longitude for 07430 is -74.1861



"""
## Code Goes Here ##

#zipcode = 10045

import requests
from pprint import pp

api_key = "e6141b5674008275c10a9b01713edabc"
country_code = "US"
zip_code = "10045"
myURL = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
results = requests.get(myURL)

print(results.status_code) #checking my status code 

myJSON = results.json() #extratcing the JSON from the response 
print(myJSON)

print('\n')

print("Pretty Print Below")
pp(myJSON)

print(type(myJSON))

###############################################################################

#New York City(MAN) 10001

import requests

from pprint import pp

api_key="e6141b5674008275c10a9b01713edabc"
country_code='US'
zip_code= str(input("Please enter a zipcode: "))
myURL= f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"

results=requests.get(myURL)

myJSON= results.json()

city = (myJSON['name'])

lat = (myJSON['lat'])

lon = (myJSON['lon'])


def user_zip(zip_code):

    if zip_code in myURL: 
        print(results.status_code)
        
        print((myJSON['name']))
        
        print(myJSON['lat'])

        print(myJSON['lon'])

    return(city, lat, lon)

print(f"The call returned code {results.status_code}\nThe city name for {zip_code} is {myJSON['name']}\nThe latitude for {zip_code} is {myJSON['lat']}\nThe longitude for {zip_code} is {myJSON['lon']}")