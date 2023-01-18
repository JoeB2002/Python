# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 01:04:46 2022

@author: Joseph Bonadeo 
"""

## now that you have a reliable way to get a lat and lon of a city, let's use it to get the weather for the city. 
## In part one of the assignment, you used the geocoding api to get the latitude and longitude of a city using its zipcode 
## copy your code from part one and now use the lat  / lon you returned to get the weather for the city

## Part 2 consists of using the current weather api
## Review the documentation of the Current Weather  API
##  https://openweathermap.org/current
## define a function to retrieve the current weather.
## Execute both the get_zip and getWeather functions to;
## print out the current city name, latitude, longitude, current weather description, current temperature, today's high and low


## Function definition
## 1. define a function called getWeather which
##  a. accepts two variables for latitude and longitude from the function you created in part 1
##  b. calls results module with the URL for weather API
##  c. returns current weather description, the current temperature, today's low and high temperatures
###
  

## Hint ###
## 1.  use the same API key you used for the get_zip function
## 2.  Follow the same steps to setup the function for weather as you did for the get_zip()
## 3.  Use the url for the current weather API found on the documentation page. 
## 4.  For the weather function in order to access the elements, look at the JSON returned. It is basically a dictionary of a set of dictionaries.
## 5.  For the temparatures, you can see in the JSON, it is part of the 'main: ' key. To access temp which is main:temp, simply assign 
##     a variable  to point the main key.  temperatures = myJSON['main'] 
##     then to get to the temperature number assign a second variable as such myTemp = temperatures['temp']
##     This allows us to go a level down in a dictionary
## 6.  For the current weather,  it is a dictionary inside a list
##     In order to access it, you will have to index it  with an offset.   weather = myJSON['weather'][0], which points to the 
##     description key. Then assign another varible to get to the value of description  weatherDESC = weather['desciption']
##     or you can assign a variable as in step 5 and include the index when accessing it. weatherDesc = weather[0]['desciption']
## 7.  Pretty Print the JSON out when writing the code, that will help you determine the key:value pair you will need. 

## Extra Credit:  use the status code returned from the weather api, to determine if a zip code is valid. An invalid zip code 
## will return a page not found code 400. 
## Extra Credit HINT - insert the test code into the get_zip() and based on the return code from the API, return values and test those values 
## in the main program.


""" Expected Output

with a valid zipcode:
    
Please enter a zipcode: 07430
The city name for 07430 is Mahwah
The latitude for 07430 is 41.0817
The longitude for 07430 is -74.1861
The current weather is overcast clouds
The current temperature is 65.1
Today's low 62.53 with a high of 68.74


with an invalid zip code for extra credit
    
Please enter a zipcode: 11111
The zipcode entered 11111 seems to be invalid.

"""


## Code Goes Here ##

print("with a valid zipcode:")

import requests

from pprint import pp

api_key="e6141b5674008275c10a9b01713edabc"
country_code='US'
zip_code = str(input("Please enter a zipcode: "))
myURL= f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"


try:
    results = requests.get(myURL)
    
    myJSON = results.json()
    
    city = (myJSON['name'])
    
    lat = (myJSON['lat'])
    
    lon = (myJSON['lon'])
    
    def kelvin_to_celsius_fahrenheit(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return round(celsius, 2), round(fahrenheit, 2)
    
    def user_zip(zip_code):
    
        if zip_code in myURL: 
            
            print((myJSON['name']))
            
            print(myJSON['lat'])
    
            print(myJSON['lon'])
    
        return(city, lat, lon)
    
    import requests, json
    
    api_key2 = "32a8b3e7966f64e45871298d48da68be"
    
    weatherURL = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key2}"
    
    results = requests.get(weatherURL)
    
    myJSON = results.json()
    
    current_weather = (myJSON['weather'][0]['description'])
    
    temp = (myJSON['main']['temp'])
    
    low_temp = (myJSON['main']['temp_min'])
    
    high_temp = (myJSON['main']['temp_max'])
    
    
    temp = kelvin_to_celsius_fahrenheit(temp)[1]
    
    low_temp = kelvin_to_celsius_fahrenheit(low_temp)[1]
    
    high_temp = kelvin_to_celsius_fahrenheit(high_temp)[1]
    
    
    def getWeather(zip_code):
        
        if zip_code in weatherURL:
            print(results.status_code)
        
            print((myJSON['description']))
            
            print((myJSON['temp']))
            
            print((myJSON['temp_min']))
        
            print((myJSON['temp_max']))
        return(current_weather, temp, low_temp, high_temp)
    
    print(f"The city name for {zip_code} is {myJSON['name']}")
    print(f"The latitude for {zip_code} is {lat}")
    print(f"The longitude for {zip_code} is {lon}")
    print(f"The current weather is {current_weather}")
    print(f"The current temperature is {temp}")
    print(f"Today's low {low_temp} with a high of {high_temp}")
    
except:
    print(f"The zipcode entered {zip_code} seems to be invalid.")
