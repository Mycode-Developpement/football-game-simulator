#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
An 11 versus 11 football game simulator project, developed by Mycode-developpement.
This is the main file executed

"""

import dispaly_console
import stats
import constant
from create_teams import create_player


import random
from colorama import Fore
import sys

class ConsoleCapture:
    def __init__(self):
        self.stdout = sys.stdout
        self.output = []

    def start_capture(self):
        sys.stdout = self

    def stop_capture(self):
        sys.stdout = self.stdout

    def write(self, text):
        self.output.append(text)

def main(action_joueur, half_time_ballon):
    global gameTime, timePerAction, halfTime
    
    temps = 0 #minutes since the start of the match
    temps_log = halfTime
    
    while temps <= gameTime:
        
        action_joueur = list_player[int(action_joueur)].Random_Action(temps, list_player)
        temps += timePerAction
        
        if int(temps) == temps_log: #half time
            
            action_joueur = half_time_ballon #ball to the team that did not have the commitment
            print(Fore.LIGHTRED_EX + "L'arbitre sifle la mi-temps ! ")
            print(Fore.LIGHTRED_EX +"Le Match reprend et la balle et pour " +  list_player[action_joueur].Return_nom() + Fore.RESET)
            temps_log = -15

    
dispaly_console.Clear()

gameTime = constant.GAME_TIME
timePerAction = constant.TIME_PER_ACTION
halfTime = constant.HALF_TIME

team1, team2 = constant.NAME_TEAM

list_player = create_player()

tirage_au_sort = random.randint(0,1)

if tirage_au_sort == 1:
    half_time_ballon = 21
    action_joueur = 10
else:
    action_joueur = 21
    half_time_ballon = 10

# start of the game 
print(Fore.LIGHTRED_EX + "L'arbitre fait le tirage au sort pour le ballon : " + "l'engagement est donc pour " + list_player[action_joueur].Return_nom() + Fore.RESET)
print()

main(action_joueur, half_time_ballon) #main function

print(Fore.LIGHTBLUE_EX + "Le match est terminé !! " + Fore.RESET)
print("")
print("")

stat1, stat2 = stats.get_stat(list_player)
stats.display_stats(stat1 , stat2, team1, team2)


#Created by Mycode Developpement