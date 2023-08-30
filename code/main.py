#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
An 11 versus 11 football game simulator project, developed by Mycode-developpement.
This is the main file executed

"""

import dispaly_console as dispaly_console
import stats as stats
import constant as constant
from create_teams import * 

import random
from colorama import Fore


def main(action_joueur, half_time_ballon):
    global gameTime, timePerAction, halfTime
    
    temps = 0 #minutes since the start of the match
    temps_log = halfTime
    
    print(Fore.LIGHTRED_EX + textLanguage[11][0] + list_player[action_joueur].Return_nom() + Fore.RESET)
    print()

    
    while temps <= gameTime:
        
        action_joueur = list_player[int(action_joueur)].Random_Action(temps, list_player)
        temps += timePerAction
        
        if int(temps) == temps_log: #half time
            
            action_joueur = half_time_ballon #ball to the team that did not have the commitment
            print(Fore.LIGHTRED_EX + textLanguage[12][0])
            print(Fore.LIGHTRED_EX +textLanguage[13][0] +  list_player[action_joueur].Return_nom() + Fore.RESET)
            temps_log = -15
    
    print(Fore.LIGHTBLUE_EX + Fore.LIGHTRED_EX +textLanguage[14][0] + Fore.RESET)
    
    print("")
    print("")
    
    stat1, stat2 = stats.get_stat(list_player)
    stats.display_stats(stat1 , stat2, team1, team2, textLanguage[15])


dispaly_console.Clear()

#get data
gameTime = constant.GAME_TIME
timePerAction = constant.TIME_PER_ACTION
halfTime = constant.HALF_TIME

team1, team2 = constant.NAME_TEAM

textLanguage = constant.TEXT_LANGUAGE[constant.LANGUAGE]

#create teams / inteligent composition

data = get_json_player()
dispo1, dispo2, adversary_team, id_dispo1, id_dispo2 = create_team_composition(data)

list_player = create_player(data, adversary_team, [id_dispo1, id_dispo2], textLanguage)

#display composition
dispaly_console.write_dispo(team1, dispo1, Fore.LIGHTYELLOW_EX, textLanguage[15][0])
dispaly_console.write_dispo(team2, dispo2, Fore.LIGHTGREEN_EX, textLanguage[15][0])

#prize draw
tirage_au_sort = random.randint(0,1)

if tirage_au_sort == 1:
    half_time_ballon = 21
    action_joueur = 10
else:
    action_joueur = 21
    half_time_ballon = 10


# start of the game 
main(action_joueur, half_time_ballon) #main function



# Created by Mycode Developpement / Youtube channel : https://www.youtube.com/@mycode-developpement