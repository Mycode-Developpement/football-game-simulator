from player import Joueur
import json
from colorama import Fore

def create_player(data, adversary_team, dispo):  
    """Fonction création de joueur appelé au démarage. C'est ici qu'il faut faire les modifications d'équipe"""

    # Create a list of opponents in the same position (striker vs. defender and midfielder vs. midfielder).
    
    list_player = []
    list_color = [[Fore.LIGHTYELLOW_EX, Fore.YELLOW], [Fore.LIGHTGREEN_EX, Fore.GREEN ]]
    
    for i, player in enumerate(data):
        list_player.append(Joueur(player['name'], player['position'], player['id'], player['pass'],player['shot'],
                                  player['goalkeeper'],player['center'],player['dribble'],player['defense'],player['interceptions'], adversary_team[i],
                                  list_color[i//11][0], list_color[i//11][1], dispo[i//11], dispo[-i//11]))
    return list_player


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
    
     #create id
    for i in range(len(sorted_data)):
        sorted_data[i]["id"] = i
            
    return sorted_data


def create_team_composition(list_player):
    """function that displays team compositions """
    team1 = list_player[:11]
    team2 = list_player[11:22]
    
    dispo1, id_dispo1 = build_dispo(team1)
    dispo2, id_dispo2 = build_dispo(team2)
    
    adversary_team1 = create_list_adversary(id_dispo1, id_dispo2)
    adversary_team2 = create_list_adversary(id_dispo2, id_dispo1)
    adversary_team1 += adversary_team2
    
    return dispo1, dispo2, adversary_team1, id_dispo1, id_dispo2
    
    
def build_dispo(team):
    """This function build the dispo team"""
    
    dispo, id_dispo = [], []
    dispo.append([team[0]["name"]])
    id_dispo.append([team[0]["id"]])
    
    before = team[0]["position"][0]
    
    assert before == "G", f"{Fore.LIGHTRED_EX}The team has no goalkeeper, it's obligatory ! {Fore.RESET}"
    
    for player in team[1:len(team)]:
        
        if player["position"][0] != before:
            dispo.append([player["name"]])
            id_dispo.append([player["id"]])
            
        else:
            dispo[-1].append(player["name"])
            id_dispo[-1].append(player["id"])
        
        before =  player["position"][0]

    return dispo, id_dispo


def create_list_adversary(id_dispo1, id_dispo2):
    adversary = []
    
    for i, sublist in enumerate(id_dispo1):
        for playerId in sublist:
            adversary.append(id_dispo2[-i])
    
    return adversary

