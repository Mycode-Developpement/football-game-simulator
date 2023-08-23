import json


def get_const_json():
    with open("Settings/settings.json", "r") as json_file:
        data = json.load(json_file) 
    return data


variable = get_const_json()

GAME_TIME = variable['timeGame']  
TIME_PER_ACTION = variable['timePerAction']    
HALF_TIME = variable['halfTime']  

NAME_TEAM = [variable['team1']['name'], variable['team2']['name']]



