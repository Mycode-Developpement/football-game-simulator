from colorama import Fore

def get_stat(list_joueur):
    # Initialisation des statistiques des deux équipes
    team1_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
               "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
               "Interception": 0}
    team2_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
                "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
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
        team_stats["Tir cadré"] += joueur.Return_Tir_Cadre()
        team_stats["Passe réussi"] += joueur.Return_Passe_Reussi()
        team_stats["Passe raté"] += joueur.Return_Passe_Rate()
        team_stats["Centre réussi"] += joueur.Return_Centre_Reussi()
        team_stats["Centre raté"] += joueur.Return_Centre_Rate()
        team_stats["Duel gagné"] += joueur.Return_Duel_Gagner()
        team_stats["Duel perdu"] += joueur.Return_Duel_Perdu()
        team_stats["Arrêt"] += joueur.Return_arret_gardien()
        team_stats["Interception"] += joueur.Return_Interception()   
        
    # Retourne les statistiques des deux équipes
    return team1_stats, team2_stats



def display_stats(team1_stats,team2_stats, team1_name, team2_name):
     # Affiche les statistiques des deux équipes
    print(f"{Fore.LIGHTRED_EX}          | {team1_name} - | - {team2_name} |")
    print(f"But :           {team1_stats['But']} | {team2_stats['But']}")
    print(f"Tir :           {team1_stats['Tir']} | {team2_stats['Tir']}")
    print(f"Tir cadré :     {team1_stats['Tir cadré']} | {team2_stats['Tir cadré']}")
    print(f"Arrêt :         {team1_stats['Arrêt']} | {team2_stats['Arrêt']}")
    print(f"Passe réussi :  {team1_stats['Passe réussi']} | {team2_stats['Passe réussi']}")
    print(f"Passe raté :    {team1_stats['Passe raté']} | {team2_stats['Passe raté']}")
    print(f"Centre réussi : {team1_stats['Centre réussi']} | {team2_stats['Centre réussi']}")
    print(f"Centre raté :   {team1_stats['Centre raté']} | {team2_stats['Centre raté']}")
    print(f"Interception :  {team1_stats['Interception']} | {team2_stats['Interception']}")
    print(f"Duel gagné :    {team1_stats['Duel gagné']} | {team2_stats['Duel gagné']}")
    print(f"Duel perdu :    {team1_stats['Duel perdu']} | {team2_stats['Duel perdu']} {Fore.RESET}")

