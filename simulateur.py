#projet de simulation de match football 
import random
from colorama import Fore
import time
import os 
from create_player import Create_player

liste_joueur = Create_player()



team1, team2 = "PSG", "Juventus"


os.system('cls') #on efface la console 
tirage_au_sort = random.randint(0,1)

if tirage_au_sort == 1:
    mi_temps_ballon = 21
    action_joueur = 10
    
else:
    action_joueur = 21
    mi_temps_ballon = 21

print(Fore.LIGHTRED_EX +"L'arbitre fait le tirage au sort pour le ballon : ")

print("L'engagement est donc pour " + liste_joueur[action_joueur].Return_nom() + " car il a mit un pouce bleu à la vidéo ! " + Fore.RESET)
temps_log = 45
temps = 0
#statistique 
###############################
but_equipe1 = 0
but_equipe2 = 0
tir_equipe1 = 0
tir_equipe2 = 0
tir_cadre_equipe1 =0
tir_cadre_equipe2 = 0
passe_reussi_equipe1 =0
passe_reussi_equipe2 = 0
passe_rate_equipe1 = 0
passe_rate_equipe2 = 0
duel_gagner_equipe1 = 0
duel_gagner_equipe2 = 0
duel_perdu_equipe1 = 0
duel_perdu_equipe2 = 0
centre_reussi_equipe1 = 0
centre_reussi_equipe2 = 0
centre_rate_equipe1 = 0
centre_rate_equipe2 = 0
interception1 = 0
interception2 = 0
arret1 = 0
arret2 = 0
###############################

#boucle du jeu 
while temps <= 90:
    action_joueur = liste_joueur[int(action_joueur)].Random_Action()
    temps += 0.09
    
    
    if int(temps) == temps_log:
        action_joueur = mi_temps_ballon #balle a l'equipe qui n'a pas eu l'engagement
        print(Fore.LIGHTRED_EX + "L'arbitre sifle la mi-temps ! ")
        print(Fore.LIGHTRED_EX +"Le Match reprend et la balle et pour " +  liste_joueur[action_joueur].Return_nom() + Fore.RESET)
        temps_log = -15
 
        

#fin du match 
print(Fore.LIGHTBLUE_EX + "Le match est terminé !! " + Fore.RESET)
print("")
print("")

num = 0
#récupération des statistiques 
while num != 22:
    
    if num <= 10:      
        but_equipe1 += liste_joueur[num].Return_But()
        tir_equipe1 += liste_joueur[num].Return_Tir()
        tir_cadre_equipe1+= liste_joueur[num].Return_Tir_Cadre()
        passe_reussi_equipe1+= liste_joueur[num].Return_Passe_Reussi()
        passe_rate_equipe1+= liste_joueur[num].Return_Passe_Rate()
        centre_reussi_equipe1 += liste_joueur[num].Return_Centre_Reussi()
        centre_rate_equipe1 += liste_joueur[num].Return_Centre_Rate()
        duel_gagner_equipe1 += liste_joueur[num].Return_Duel_Gagner()
        duel_perdu_equipe1 += liste_joueur[num].Return_Duel_Perdu()
        arret1 += liste_joueur[num].Return_arret_gardien()
        interception1 += liste_joueur[num].Return_Interception()
        
        
    
    else:    
        but_equipe2 += liste_joueur[num].Return_But()
        tir_equipe2 += liste_joueur[num].Return_Tir()
        tir_cadre_equipe2+= liste_joueur[num].Return_Tir_Cadre()
        passe_reussi_equipe2+= liste_joueur[num].Return_Passe_Reussi()
        passe_rate_equipe2+= liste_joueur[num].Return_Passe_Rate()
        centre_reussi_equipe2 += liste_joueur[num].Return_Centre_Reussi()
        centre_rate_equipe2 += liste_joueur[num].Return_Centre_Rate()
        duel_gagner_equipe2 += liste_joueur[num].Return_Duel_Gagner()
        duel_perdu_equipe2 += liste_joueur[num].Return_Duel_Perdu()
        arret2 += liste_joueur[num].Return_arret_gardien()
        interception2 += liste_joueur[num].Return_Interception()
    
    num += 1
print(Fore.LIGHTRED_EX + f"          | {team1} - | - {team2} |")
print("But :           " + str(but_equipe1) + " | " + str(but_equipe2))
print("Tir :           " + str(tir_equipe1) + " | " + str(tir_equipe2))
print("Tir cadré :     " + str(tir_cadre_equipe1) + " | " + str(tir_cadre_equipe2))
print("Arrêt :         " + str(arret1) + " | " + str(arret2))
print("Passe réussi :  " + str(passe_reussi_equipe1) + " | " + str(passe_reussi_equipe2))
print("Passe raté :    " + str(passe_rate_equipe1) + " | " + str(passe_rate_equipe2))
print("Centre réussi : " + str(centre_reussi_equipe1) + " | " + str(centre_reussi_equipe2))
print("Centre raté :   " + str(centre_rate_equipe1) + " | " + str(centre_rate_equipe2))
print("interception :  " + str(interception1) + " | " + str(interception2))
print("Duel gagné :    " + str(duel_gagner_equipe1) + " | " + str(duel_gagner_equipe2))
print("Duel perdu :    " + str(duel_perdu_equipe1) + " | " + str(duel_perdu_equipe2))
