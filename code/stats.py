from colorama import Fore
from prettytable import PrettyTable


def get_stat(list_joueur):
    # Initialisation des statistiques des deux équipes
    team1_stats = {"But": 0, "Tir": 0, "Tir_cadré": 0, "Passe_réussi": 0, "Passe_raté": 0, 
               "Centre_réussi": 0, "Centre_raté": 0, "Duel_gagné": 0, "Duel_perdu": 0, "Arrêt": 0,
               "Interception": 0}
    team2_stats = {"But": 0, "Tir": 0, "Tir_cadré": 0, "Passe_réussi": 0, "Passe_raté": 0, 
                "Centre_réussi": 0, "Centre_raté": 0, "Duel_gagné": 0, "Duel_perdu": 0, "Arrêt": 0,
                "Interception": 0}

    # Parcours des joueurs de la liste des joueurs
    for joueur in list_joueur:
        # Si le numéro du joueur est inférieur ou égal à 10, il appartient à l'équipe 1, sinon il appartient à l'équipe 2
        if joueur.num <= 10:
            team_stats = team1_stats
        else:
            team_stats = team2_stats
        
        # Mise à jour des statistiques de l'équipe correspondante en fonction des statistiques du joueur
        team_stats["But"] += joueur.Return_But()
        team_stats["Tir"] += joueur.Return_Tir()
        team_stats["Tir_cadré"] += joueur.Return_Tir_Cadre()
        team_stats["Passe_réussi"] += joueur.Return_Passe_Reussi()
        team_stats["Passe_raté"] += joueur.Return_Passe_Rate()
        team_stats["Centre_réussi"] += joueur.Return_Centre_Reussi()
        team_stats["Centre_raté"] += joueur.Return_Centre_Rate()
        team_stats["Duel_gagné"] += joueur.Return_Duel_Gagner()
        team_stats["Duel_perdu"] += joueur.Return_Duel_Perdu()
        team_stats["Arrêt"] += joueur.Return_arret_gardien()
        team_stats["Interception"] += joueur.Return_Interception()   
        
    # Retourne les statistiques des deux équipes
    return team1_stats, team2_stats



def display_stats(team1_stats,team2_stats, team1_name, team2_name, text):
     # Affiche les statistiques des deux équipes
     
    tab = PrettyTable()
    tab.padding_width = 5

    tab.field_names = [f"{Fore.CYAN}{text[1]}", team1_name, team2_name + Fore.RESET]

    for i,element in enumerate(team1_stats):
        tab.add_row([Fore.CYAN + text[i+2] + Fore.RESET, team1_stats[element], team2_stats[element]])

    print(tab)

