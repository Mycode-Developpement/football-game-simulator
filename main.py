#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
An 11 versus 11 football game simulator project, developed by Mycode-developpement.
This is the main file executed

"""

import dispaly_console
import stats
from create_teams import create_player

import random
from colorama import Fore


def main(action_joueur, mi_temps_ballon):
    temps = 0 #minutes since the start of the match
    temps_log = 45
    while temps <= 90:
        action_joueur = list_player[int(action_joueur)].Random_Action(temps, list_player)
        temps += 0.09
        if int(temps) == temps_log: #half time
            action_joueur = mi_temps_ballon #ball to the team that did not have the commitment
            print(Fore.LIGHTRED_EX + "L'arbitre sifle la mi-temps ! ")
            print(Fore.LIGHTRED_EX +"Le Match reprend et la balle et pour " +  list_player[action_joueur].Return_nom() + Fore.RESET)
            temps_log = -15
    
    
dispaly_console.Clear()

team1, team2 = "PSG", "Juventus"

list_player = create_player()

tirage_au_sort = random.randint(0,1)

if tirage_au_sort == 1:
    mi_temps_ballon = 21
    action_joueur = 10
else:
    action_joueur = 21
    mi_temps_ballon = 10

# start of the game
print(Fore.LIGHTRED_EX + "L'arbitre fait le tirage au sort pour le ballon : ")
print("L'engagement est donc pour " + list_player[action_joueur].Return_nom() + Fore.RESET)

main(action_joueur, mi_temps_ballon) #main function

print(Fore.LIGHTBLUE_EX + "Le match est terminé !! " + Fore.RESET)
print("")
print("")

stat1, stat2 = stats.get_stat(list_player)
stats.display_stats(stat1 , stat2, team1, team2)


#Created by Mycode Developpement