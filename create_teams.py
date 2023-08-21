from player import Joueur
import json

def create_player():  
    """Fonction création de joueur appelé au démarage. C'est ici qu'il faut faire les modifications d'équipe"""
    
    data = get_json_player()
    
    list_player = []
    
    for player in data:
        list_player.append(Joueur(player['name'], player['position'], player['number'], player['pass'],player['shot'],
                                  player['goalkeeper'],player['center'],player['dribble'],player['defense'],player['interceptions']))
    return list_player


def get_json_player():
    """get player data from json file"""
    
    with open("Settings/team1.json", "r") as json_file:
        data = json.load(json_file) #team 1
    
    with open("Settings/team2.json", "r") as json_file:
        data += json.load(json_file) #team 2
    
    return data