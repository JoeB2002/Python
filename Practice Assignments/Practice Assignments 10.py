# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 11:38:30 2022

@author: Joseph Bonadeo
"""
##  In class challenge
## we are going to scrape a listing of apartments in NYC. For each apartment we are going to scrape the following:
## Name of the building or title
## Address of the building
## The rental price
## Number of bedrooms

## I have included the import statments below and the URL and Headers as well as hints on the steps. Add your code after the comments in
## each section to build the screenscraper.

from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.apartments.com/new-york-ny/?bb=1ygqrl-pwHgjhv4pC"
headers = {"Content-Type":"application/json", "User-agent":"Mozilla"}


## Load up the URL into a variable, use requests to retrieve it and also send the headers in with the URL. Print the page to make sure
## we get the 200 code

page = requests.get(url, headers=headers) # My web page

print(page.status_code)

print('\n')
## Soupify the page using the html.parser

soup = BeautifulSoup(page.content, "html.parser") # soupify the webpage


list = soup.find_all("li",class_ = "mortar-wrapper")

print(list)

## load the page in a modern browser, inspect the page and find the highest level tag which will give you all of the info you need

lists = soup.find_all("li",class_ = "mortar-wrapper")
for list in lists:
    title = list.find("span", class_ = "js-placardTitle title").text
    address = list.find("div", class_= "property-address js-url").text
    print(title)
    print(address)

# using the with open() , open a csv file for write.
## write the column headers to the file
## Iterate through the tags and write the data out to the file. 

lists = soup.find_all("li",class_ = "mortar-wrapper")
thewriter = writer(f)
thewriter.writerow(header)
for list in lists:
    title = list.find("span", class_ = "js-placardTitle title").text
    address = list.find("div", class_= "property-address js-url").text
    rent = list.find("div", class_= "property-rest js-url").text
    address = list.find("div", class_= "property-bedroom js-url").text
    print(title)
    print(address)
    info = [title,address,rent,bedroom]
    thewriter.writerow(info)

