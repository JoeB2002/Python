from sportsreference.nfl.teams import Teams
import requests
from bs4 import BeautifulSoup
import json
import sys

#gets user data for getTeam()
typedInName = input("Please enter a NFl Team name or one word out of the name: ")

def getTeam():

    url = "https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/win-stats/2020"
    
    headers = {
        "X-RapidAPI-Key": "1e2e9e3fabmshd5d95ad5f5d0235p18ce1ejsne741590d0bb0",
        "X-RapidAPI-Host": "nfl-team-stats.p.rapidapi.com"
    }
    
    #get the data from rapidapi api
    response = requests.request("GET", url, headers=headers)
    results = response.text
    
    
    #convert the response to a dict
    jdata = json.loads(results)
    
    #get the team list from the dict
    teamList = jdata['_embedded']['teamWinStatsList']
    
    #sets varibles to global meaning the rest of the program can recognize it
    global name
    global wins
    global losses
    global WRP
    
    #search through the list for team names containing the typed in name. convert both to lower to prevent case mismatches.
    for item in teamList:
        if typedInName.lower() in item['name'].lower():
    #        print(item)
            
            #get one of the properties
            name = item['name']
            name = name.replace("xz*","").replace("xz","")
    #        print(name)
            
            wins = item['wins']
    #        print(wins)
            
            losses = item['losses']
    #        print(losses)
     
            WRP = item['winRatePercentage']
    #        print(WRP)
    
    #NameError handling
    print()
    try:
        print('Team name selected:',name)
    except NameError:
        print('Invalid Name, please run again')
        sys.exit()
    print()
    
    return name,wins,losses,WRP

getTeam()

WRPRounded=100*WRP

#prints the data returned from getTeam()
print(f"The team {name} has {wins} wins & {losses} losses. This gives them a win percentage of {WRPRounded}%") 
