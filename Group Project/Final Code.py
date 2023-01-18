# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:43:46 2022

@author: Owner
"""

from nba_api.stats.static import players
import requests
import json
import sys
player_dict = players.get_players()
from nba_api.stats.endpoints import playercareerstats

def getTeam(teamName):
    
    url = "https://api-nba-v1.p.rapidapi.com/teams"

    headers = {
    	"X-RapidAPI-Key": "61c62e4682mshe3a2cd9bac1a25bp1b8fa9jsn656cf1757ae1",
    	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
      
    #get the data from rapidapi api
    response = requests.request("GET", url, headers=headers)
    results = response.text

    
    #convert the response to a dict
    jdata = json.loads(results)
    
    #get the team list from the dict
    teamList = jdata['response']
    
    #sets varibles to global meaning the rest of the program can recognize it
    global fgm
    global fgp
    global assists
    global teamDetail
    global name
    
    
    #search through the list for team names containing the typed in name. convert both to lower to prevent case mismatches.
    for item in teamList:
        if teamName.lower() in item['name'].lower():
            
            #get one of the properties
            id1 = item['id']
            name = item['name']
            
            url2 = "https://api-nba-v1.p.rapidapi.com/teams/statistics"
            querystring = {"id":id1,"season":"2022"}
            
            response2 = requests.request("GET", url2, headers=headers, params=querystring)
            results2 = response2.text

            #convert the response to a dict
            jdata2 = json.loads(results2)
            
            #get the team list from the dict
            teamDetail = jdata2['response'][0]
            
            #print(teamDetail)

            fgm = teamDetail['fgm']
         
            fgp = teamDetail['fgp']

            assists = teamDetail['assists']
        
#NameError handling
    print()
    try:
        print('Team name selected:',name)
    except NameError:
        print('Invalid Name, please run again')
        sys.exit()
    print()

uInput = input("Please input the letter 't' for team data, or 'p' for players. If you with to quit this program please input 'q'")

if uInput=='t':
    userIn = input("Please enter a team to see the stats: ")
    mydata = getTeam(userIn)
    print(f"The team {name} has {fgm} Field Goals Made & a {fgp}% Field Goal Percentage. They also have a team combined total of {assists} assists.") 

def getPlayerStats():
    global player_info
    player_info = [player for player in player_dict if player['full_name'].lower() == player_fullname.lower()][0]
    player_id = player_info['id']    
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    global career_df
    career_df=career_stats.get_data_frames()[1]
    career_df[player_fullname]=player_info['full_name']    
    blankIndex=[''] * len(career_df)
    career_df.index=blankIndex
    return career_df
    
        
if uInput.lower()=='p':
    player_fullname=input("Please input your player's full name with a space between first and last name here: ")
    try:
     getPlayerStats()
    except:
        print('Quitting application, have a nice day!')
        sys.exit()
    print('Total Current Career Stats for player:')
    print(career_df[['PTS','FT_PCT','OREB','DREB','REB','AST','STL','BLK','TOV','PF']])
    print()
    print('Total Current Career Stats continued:')
    print(career_df[['GP','GS','MIN','FGM','FGA','FG_PCT','FG3A','FG3_PCT','FTM','FTA']])

if uInput=='q':
    print('Quitting application, have a nice day!')
    sys.exit()