import requests

headers = {"Content-Type":"application/json", "User-agent":"Mozilla"}

results = requests.get('http://api.open-notify.org/astros.json', headers=headers)

myJSON  = results.json()

print(myJSON)

###############################################################################
print('\n')
###############################################################################

print (myJSON['message'])

###############################################################################
print('\n')
###############################################################################

print(results.status_code)

###############################################################################
print('\n')
###############################################################################
print('The people currently in space are:')

for p in myJSON['people']:

    print(p['name'])
    
###############################################################################
print('\n')
###############################################################################    
    
print('The people currently in space are:')

for p in myJSON['people']:

    print(f"{p['craft']} : {p['name']}")
    
###############################################################################
print('\n')
###############################################################################      
    
import requests

from pprint import pp # prettify my return JSON

results = requests.get('http://api.open-notify.org/astros.json')

myJSON  = results.json()

print (myJSON['message'])

print(myJSON)

pp(myJSON)