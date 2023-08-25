from player import Joueur
import json

def create_player():  
    """Fonction création de joueur appelé au démarage. C'est ici qu'il faut faire les modifications d'équipe"""
    
    data = get_json_player()
    
    list_player = []
    
    for player in data:
        list_player.append(Joueur(player['name'], player['position'], player['number'], player['pass'],player['shot'],
                                  player['goalkeeper'],player['center'],player['dribble'],player['defense'],player['interceptions']))
    return list_player, data


def get_json_player():
    """get player data from json file"""
    
    order_of_position = [
        "G", "DD", "DC", "DG", "MC", "AD", "AC", "AG"
    ]
    
    with open("../Settings/team1.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file) #team 1
        data = data["player"][:11]
        sorted_data = sorted(data, key=lambda x: order_of_position.index(x["position"]))

    with open("../Settings/team2.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file) #team 2
        data = data["player"][:11]
        sorted_data += sorted(data, key=lambda x: order_of_position.index(x["position"]))
    
    return sorted_data


def create_team_composition(list_player, nameTeam1, nameTeam2):
    """function that displays team compositions """
    team1 = list_player[:11]
    team2 = list_player[11:22]
    
    dispo1 = build_dispo(team1)
    dispo2 = build_dispo(team2)
    
    return dispo1, dispo2
    
    
def build_dispo(team):
    """This function build the dispo team"""
    
    dispo = []
    dispo.append([team[0]["name"]])
    
    before = team[0]["position"][0]
    
    for player in team[1:len(team)]:
        
        if player["position"][0] != before:
            dispo.append([player["name"]])
            
        else:
            dispo[-1].append(player["name"])
        
        before =  player["position"][0]
    
    return dispo