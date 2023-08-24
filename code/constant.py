import json


def get_const_json(path):
    with open(path, "r") as json_file:
        data = json.load(json_file) 
    return data


variable = get_const_json("../Settings/settings.json")

GAME_TIME = variable['timeGame']  
TIME_PER_ACTION = variable['timePerAction']    
HALF_TIME = variable['halfTime']  

variable = get_const_json("../Settings/team1.json")
variable2 = get_const_json("../Settings/team2.json")

NAME_TEAM = [variable['name'], variable2['name']]



