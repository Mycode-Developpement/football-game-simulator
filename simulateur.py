#!/usr/bin/python
# -*- coding: utf-8 -*-


#projet de simulation de match football 11 contre 11
import random
from colorama import Fore
import time
import os 

class Joueur ():
    """Class Joueur : permet de créer les joueurs des deux équipes numéroté id entre 0 et 21"""    
    def __init__(self, nom, poste, num, passe, tir, arret, centre, dribble, defense, interception ):
        self.nom = nom
        self.poste = poste
        self.num = num
        self.passe = passe
        self.tir = tir 
        self.note_arret = arret
        self.centre = centre
        self.dribble = dribble
        self.defense = defense
        self.interception = interception
        
        #stat pour ceux du match en particulier 
        
        self.nombre_but = 0
        self.nombre_tir_cadre = 0
        self.nombre_tir = 0
        self.passe_reussi = 0
        self.passe_rate = 0
        self.centre_reussi = 0
        self.centre_rate = 0
        self.duel_gagne = 0
        self.duel_perdu = 0
        self.arret = 0
        self.nombre_interception = 0
        self.degagement_reussi = 0
        self.degagement_rate = 0
        
        #poste de chaque joueur 
        self.attaque1 = [8,9,10,]
        self.attaque2 = [19,20,21]
        self.milieux1 = [5,6,7]
        self.milieux2 = [16,17,18]
        self.defenseur1 = [1,2,3,4]
        self.defenseur2 = [12,13,14,15]
        
        self.minute = 0
    
    #fonction qui donne des info sur le joueur. 
    def Return_nom(self):
        return self.nom

    def Return_note_arret_gardien(self):
        return self.note_arret
    
    def Return_note_defense(self):
        return self.defense
    
    def Return_note_interception(self):
        return self.interception
    
    def Arret_gardien(self):
        self.arret += 1 
        
    def Duel_gagner(self):
        self.duel_gagne += 1 
        
    def Duel_perdu(self):
        self.duel_perdu += 1
        
    def Interception_reussi(self):
        self.nombre_interception += 1
        
    #stat
    
    def Return_Tir(self):
        return self.nombre_tir
    
    def Return_Tir_Cadre(self):
        return self.nombre_tir_cadre
    
    def Return_But(self):
        return self.nombre_but
    
    def Return_Passe_Reussi(self):
        return self.passe_reussi
    
    def Return_Passe_Rate(self):
        return self.passe_rate
    
    def Return_Centre_Reussi(self):
        return self.centre_reussi
    
    def Return_Centre_Rate(self):
        return self.centre_rate
    
    def Return_Interception(self):
        return self.nombre_interception 
    
    def Return_Duel_Gagner(self):
        return self.duel_gagne
    
    def Return_Duel_Perdu(self):
        return self.duel_perdu
    
    def Return_arret_gardien(self):
        return self.arret
        
    def Random_Action (self):
        """Fonction principale appelé lors de chaque action : 
        - Aucun paramatre en entré
        - En sortie le numéro du joueur qui a maintenant la balle 
        Cette fonction varie selon le poste du joueur. 
        """
        global liste_joueur, temps
        self.minute = int(temps)
        #code executé quand le joueur recoit le ballon
        if self.poste == "BU":
            random_action = random.randint(0,60)
            if random_action == 1:
                #tir dans la surface 
                return self.Tir_dans_la_surface()
            
            elif random_action == 2:
                return self.Tir_hors_surface()
            
            elif random_action == 3 or random_action == 4:
                return self.Passe_courte()
            
            elif random_action == 5:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        
        elif self.poste == "AG" or self.poste == "AD":
            random_action = random.randint(0,60)
            if random_action == 2:
                #tir dans la surface 
                return self.Tir_dans_la_surface()
            
            elif random_action <= 4:
                return self.Tir_hors_surface()
            
            elif random_action <= 7:
                return self.Centre()
            
            elif random_action <= 12:
                return self.Passe_courte()
            
            elif random_action == 30:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        
        elif self.poste == "MC":
            random_action = random.randint(0,90)
            if random_action == 1:
                return self.Tir_hors_surface()
            
            elif random_action <= 15:
                return self.Passe_courte()
            
            elif random_action <= 20:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        elif self.poste == "DD" or self.poste == "DG":
            random_action = random.randint(0,30)
            
            if random_action == 1:
                return self.Centre()
            
            elif random_action <= 10:
                return self.Passe_courte()
            
            elif random_action == 11:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        
          
        elif self.poste == "DC":
            random_action = random.randint(0,20)
            
            if random_action <= 3:
                return self.Passe_courte()
            
            elif random_action == 4:
                return self.Degagement()
            
            elif random_action == 6:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        else: #gardien
            random_action = random.randint(0,6)
            
            if random_action == 1:
                return self.Passe_courte()
            
            elif random_action == 2:
                return self.Degagement()
            
            else: #passe
                return self.Passe()
            

    def Passe(self):
        global liste_joueur
        self.action = self.num 
        random_note = random.randint(0,95)  #note aléatoire qui permet de savoir si un geste est réussi
        
        if random_note > self.passe:
            #passe raté
            if self.num <= 10:   
                self.action = random.randint(11,21)
            else:
                self.action = random.randint(0,10)
            
            #print(self.nom + " a raté sa passe ! ")
            self.passe_rate += 1 #passe raté
        
        else: #passe réussi 
            
            #maintenant il faut verifier si ce n'est pas intercepté
            
            if self.num <= 10:
                defenseur = self.defenseur2
            else:
                defenseur = self.defenseur1
            
            #choisir l'adversaire qui peut couper le centre 
            adversaire = random.choice(defenseur)
            note_defense = liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
            random_note = random.randint(0,6000)
            
            if random_note > note_defense:
                if self.num <= 10:           
                    while self.action == self.num : 
                        #le joueur ne peut pas se faire une passe a lui même 
                        self.action = random.randint(0,10)
                else:
                    while self.action == self.num : 
                        #le joueur ne peut pas se faire une passe a lui même 
                        self.action = random.randint(11,21)
                    
                self.passe_reussi += 1 
                #print(self.nom + " a réussi sa passe en direction de " + liste_joueur[self.action].Return_nom())


            else:
                #le defenseur la coupe 
                self.action = adversaire
                self.passe_rate += 1
                liste_joueur[self.action].Interception_reussi() #+1
                #print( Fore.LIGHTBLUE_EX + self.nom + " réussi sa passe mais "+ liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
    
        return self.action
    
    
    
    def Tir_dans_la_surface(self):
        global liste_joueur   
        random_note = random.randint(0,130)
        self.nombre_tir += 1 
        self.minute = int(temps)
        
        if random_note > self.tir : 
            #le tir est raté
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
                # On rend la balle au gardien 
                
            print (Fore.CYAN +self.nom + " a tiré dans la surface mais n'a pas réussi à cadré ! Balle pour le gardien adverse. (" + str(self.minute) + "min) " + Fore.RESET)
            
            
        
        else:
            #le tir est cadré 
            #il faut verifier si le gardien adverse arrive a faire l'arrêt ou pas         
            if self.num <= 10:
                #le gardien adverse est donc le numéro 11
                note_arret_gardien = liste_joueur[11].Return_note_arret_gardien()
                num_gardien = 11
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = liste_joueur[0].Return_note_arret_gardien()
                num_gardien = 0
                engagement = 11
            
            random_note = random.randint(0,130) #savoir si le gardien l'arrête
            
            if random_note > note_arret_gardien:
                #il y a donc but 
                print("")
                print(Fore.RED + self.nom + " a tiré dans la surface et a marqué !!! But !! ("  + str(self.minute) + "min) ")
                print(Fore.RESET + "\n")
                self.action = engagement
                self.nombre_but += 1
                self.nombre_tir_cadre += 1
               

            else:
                #le gardien l'arrete, il garde la balle 
                self.action = num_gardien
                print(Fore.GREEN + self.nom + " a tiré dans la surface surface mais le gardien l'a arrêter ! (" + str(self.minute) + "min) ")
                print(Fore.RESET + "\n")
                self.nombre_tir_cadre += 1
                liste_joueur[self.action].Arret_gardien() #+1 arret
                
 
        return self.action
    
    
    def Tir_hors_surface(self):
        global liste_joueur   
        random_note = random.randint(0,150) 
        self.nombre_tir += 1
        
        if random_note > self.tir : 
            #le tir est raté
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
                # On rend la balle au gardien 
            print (self.nom + " a tiré en dehors de la surface et n'a pas réussi à cadré ! Balle pour le gardien adverse. ("  + str(self.minute) + "min) ")
        
        else:
            #le tir est cadré 
            #il faut verifier si le gardien adverse arrive a faire l'arrêt ou pas         
            if self.num <= 10:
                #le gardien adverse est donc le numéro 11
                note_arret_gardien = liste_joueur[11].Return_note_arret_gardien()
                num_gardien = 11
                
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = liste_joueur[0].Return_note_arret_gardien() + random.randint(0,6)
                num_gardien = 0
                engagement = 11
            
            random_note = random.randint(0,100) #savoir si le gardien l'arrête
            
            if random_note > note_arret_gardien:
                #il y a donc but 
                print()
                print(Fore.RED + self.nom + " a tiré hors de la surface et a marqué !!! But !! ("  + str(self.minute) + "min) ")
                print(Fore.RESET + "\n")
                self.action = engagement
                self.nombre_but += 1
                self.nombre_tir_cadre += 1
             

            else:
                #le gardien l'arrete, il garde la balle 
                self.action = num_gardien
                print(Fore.GREEN + self.nom + " a tiré hors de la surface mais le gardien l'a arrêter ! ("  + str(self.minute) + "min) ")
                self.nombre_tir_cadre += 1
                print(Fore.RESET + "\n")
                liste_joueur[self.action].Arret_gardien()
          
        return self.action
    
    
    def Centre(self):
        #centre des latéraux ! 
        global liste_joueur
        
        random_note = random.randint(0,105)
        
        if random_note > self.centre:
            # sors en 6 mètre 
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
            print(Fore.BLUE+ self.nom + " a raté son centre qui file en sorti de but (" + str(self.minute) + "min) " + Fore.RESET)
            
            self.centre_rate += 1

        else:
            #centre réussi
            if self.num <= 10:
                if self.num == 10 or self.num == 5:
                    self.action = random.randint(8,9)
                else:
                    self.action = random.randint(9,10)
               
            
            else:
                if self.num == 21:
                    self.action = random.randint(19,20)
                else:
                    self.action = random.randint(20,21)
                    
            #maintenant il faut verifier si ce n'est pas intercepté
            
            if self.num <= 10:
                defenseur = self.defenseur2
            else:
                defenseur = self.defenseur1
            
            #choisir l'adversaire qui peut couper le centre 
            adversaire = random.choice(defenseur)
            note_defense = liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
            random_note = random.randint(0,160)
            
            if random_note > note_defense:
                print( Fore.YELLOW + self.nom + " réussi son centre vers " + liste_joueur[self.action].Return_nom()  + " ("+ str(self.minute) + "min) "+ Fore.RESET)
                self.centre_reussi += 1 
                return liste_joueur[self.action].Tir_dans_la_surface() #il tir obligatoirement car le defenseur ne la touche pas 


            else:#le defenseur la coupe 
                self.action = adversaire
                
                print( Fore.YELLOW + self.nom + " réussi son centre mais "+ liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! (" + str(self.minute) + "min) "+ Fore.RESET)
                
                self.centre_rate += 1
                liste_joueur[self.action].Interception_reussi()
    
        return self.action
    
    def Passe_courte(self):
        global liste_joueur
        random_note = random.randint(0,95)  #note aléatoire qui permet de savoir si un geste est réussi
        
        if random_note > self.passe:
            #passe raté
            if self.num <= 10:   
                self.action = random.randint(11,21)
            else:
                self.action = random.randint(0,10)
            
            #print(self.nom + " a raté sa passe courte ! ")
            self.passe_rate += 1
        else:
            
            if self.num == 0 or  self.num == 11:            
                self.action = self.num + 1
                #ne peut pas faire de passe au joueur plus en bas car ce sont les gardiens 
             
            elif self.num == 10 or  self.num == 21:            
                self.action = self.num - 1
                #peut juste faire une passe courte au joueur d'avant car personne après 
            
            else:
                random_note = random.randint(0,1)
                if random_note == 0:
                    self.action = self.num - 1
                else:
                    self.action = self.num + 1
                    
            #print(self.nom + " a réussi sa passe courte vers " + liste_joueur[self.action].Return_nom())
            self.passe += 1
        
        return self.action
    
    
    def Degagement(self):
        global liste_joueur
        random_note = random.randint(0,130)  #note aléatoire qui permet de savoir si un geste est réussi
        
        if random_note > self.passe:
            #degagement raté
            if self.num <= 10:   
                self.action = random.randint(12,18)
            else:
                self.action = random.randint(1,7)
            
            #print(self.nom + " a raté son degagement, recupération :  " + liste_joueur[self.action].Return_nom() ) 
            
        
        else:
            
            #maintenant il faut verifier si ce n'est pas intercepté
            
            if self.num <= 10:
                defenseur = self.defenseur2
            else:
                defenseur = self.defenseur1
            
            #choisir l'adversaire qui peut couper le centre 
            adversaire = random.choice(defenseur)
            note_defense = liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
            random_note = random.randint(0,125)
            
            if random_note > note_defense: #la passse n'est pas intercepté 
                    
                #réussi
                self.action = self.num
                
                if self.num <= 10:   
                    while self.action == self.num:
                        self.action = random.randint(1,7)
                else:
                    while self.action == self.num:
                        self.action = random.randint(12,18)
                
                #print(self.nom + " a réussi son degagement vers :  " + liste_joueur[self.action].Return_nom() )   
                
           
            else: #le defenseur l'intercepte 
                self.action = adversaire
                
                liste_joueur[self.action].Interception_reussi()
                #print( Fore.CYAN + self.nom + " réussi son degagement mais "+ liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
             
        
        return self.action 
    
    
    def Duel(self):
        global liste_joueur  
        #defense par zone 
        #trouver le joueur qui va defendre dessus par rapport au positionnement 
        if self.num in self.attaque1:
            adversaire = random.choice(self.defenseur2)
        
        elif self.num in self.attaque2:
            adversaire = random.choice(self.defenseur1)
        
        elif self.num in self.milieux1:
            adversaire = random.choice(self.milieux2)
        
        elif self.num in self.milieux2:
            adversaire = random.choice(self.milieux1)
        
        elif self.num in self.defenseur1:
            adversaire = random.choice(self.attaque2)
        
        elif self.num in self.defenseur2:
            adversaire = random.choice(self.attaque1)
            
        #on a maintenant l'adversaire 
        note_defense_adversaire = liste_joueur[adversaire].Return_note_defense()
        note_attaque = self.dribble + random.randint(0,5)
        note_defense_adversaire += random.randint(0,5)
        
        if note_attaque >= note_defense_adversaire:
            #dribble réussi
            self.action = self.num
            
            self.duel_gagne += 1 
            
            liste_joueur[adversaire].Duel_perdu()
            if random.randint(1,5) == 2:
                print(self.nom + " a gagné son duel face à " + liste_joueur[adversaire].Return_nom() + " grâce a un super geste technique ! (" + str(self.minute)+ "min) ")
        else:
            self.action = adversaire
            self.duel_perdu += 1
            liste_joueur[self.action].Duel_gagner()
            if random.randint(1,5) == 2:
                print(self.nom + " a perdu son duel face à " + liste_joueur[adversaire].Return_nom() + " (" + str(self.minute) + "min) " )
        

        return self.action


def recup_stat():
    # Initialisation des statistiques des deux équipes
    team1_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
               "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
               "Interception": 0}
    team2_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
                "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
                "Interception": 0}

    # Parcours des joueurs de la liste des joueurs
    for joueur in liste_joueur:
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

def afficher_stat(team1_stats,team2_stats):
     # Affiche les statistiques des deux équipes
    print(f"{Fore.LIGHTRED_EX}          | {team1} - | - {team2} |")
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

def creation_joueur():  
    """Fonction création de joueur appelé au démarage. C'est ici qu'il faut faire les modifications d'équipe"""
    liste_joueur = []
    liste_joueur.append(Joueur("Donnarumma", "G",0,56,0,90,0,0,0,0,))
    liste_joueur.append(Joueur("Hakimi", "DD", 1, 81, 68, 0, 77, 79,76,78))
    liste_joueur.append(Joueur("Ramos", "DC", 2,78, 0,0,0,63,83,84))
    liste_joueur.append(Joueur("Marquinhos", "DC", 3,84, 0,0,0,69,89,89))
    liste_joueur.append(Joueur("Mendès", "DG", 4,77,0,0,66,77,75,74))
    liste_joueur.append(Joueur("Veratti", "MC", 5,90,58,0,0,91,80,85))
    liste_joueur.append(Joueur("Vitinha", "MC", 6,85,71,0,0,82,70,73))
    liste_joueur.append(Joueur("Sanches", "MC", 7,81,78,0,0,84,70,75))
    liste_joueur.append(Joueur("Messi", "AD", 8,91,90,0,87,95,32,34))
    liste_joueur.append(Joueur("Mbappé", "BU",9,85,90,0,80,93,30,38))
    liste_joueur.append(Joueur("Neymar", "AG",10,85,83,0,80,95,30,37))

    liste_joueur.append(Joueur("Szczęsny", "G", 11,56,0,86,0,0,0,0))
    liste_joueur.append(Joueur("Cuadrado", "DD", 12,81,65,0,84,90,80,73))
    liste_joueur.append(Joueur("Bonucci", "DC", 13,81,0,0,0,69,82,86))
    liste_joueur.append(Joueur("Bremer", "DC", 14,69,0,0,0,62,84,84))
    liste_joueur.append(Joueur("Alex Sandro", "DG", 15,75,0,0,82,78,78,75))
    liste_joueur.append(Joueur("Locatelli", "MC", 16,85,80,0,0,78,77,79))
    liste_joueur.append(Joueur("McKennie", "MC", 17,79,73,0,0,81,79,79))
    liste_joueur.append(Joueur("Zakaria", "MC", 18,79, 63,0,0,78,80,80))
    liste_joueur.append(Joueur("Di María", "AD", 19,82,82,0,85,88,53,42))
    liste_joueur.append(Joueur("Vlahović", "BU",20,73, 88, 0,57,80,25,25))
    liste_joueur.append(Joueur("Kean", "AG",21,68,79,0,48,79,30,31))
    return liste_joueur

def Clear():
    """Fonction qui nettoye la console"""
    if os.name == 'nt': # si le système d'exploitation est Windows
        os.system('cls') # effacer la console
    else: # sinon
        os.system('clear') # effacer la console

liste_joueur = creation_joueur()
# définition des noms des équipes
team1, team2 = "PSG", "Juventus"

Clear()
    
temps = 0 #minutes depuis le début de la rencontre 
tirage_au_sort = random.randint(0,1)

if tirage_au_sort == 1:
    mi_temps_ballon = 21
    action_joueur = 10
    
else:
    action_joueur = 21
    mi_temps_ballon = 10

print(Fore.LIGHTRED_EX +"L'arbitre fait le tirage au sort pour le ballon : ")
print("L'engagement est donc pour " + liste_joueur[action_joueur].Return_nom() + " car il a mit un pouce bleu à la vidéo ! " + Fore.RESET)
temps_log = 45

##boucle du jeu 
while temps <= 90:
    action_joueur = liste_joueur[int(action_joueur)].Random_Action()
    temps += 0.09
    if int(temps) == temps_log:
        action_joueur = mi_temps_ballon #balle a l'equipe qui n'a pas eu l'engagement
        print(Fore.LIGHTRED_EX + "L'arbitre sifle la mi-temps ! ")
        print(Fore.LIGHTRED_EX +"Le Match reprend et la balle et pour " +  liste_joueur[action_joueur].Return_nom() + Fore.RESET)
        temps_log = -15
 
    
print(Fore.LIGHTBLUE_EX + "Le match est terminé !! " + Fore.RESET)
print("")
print("")

team1_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
               "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
               "Interception": 0}
team2_stats = {"But": 0, "Tir": 0, "Tir cadré": 0, "Passe réussi": 0, "Passe raté": 0, 
               "Centre réussi": 0, "Centre raté": 0, "Duel gagné": 0, "Duel perdu": 0, "Arrêt": 0,
               "Interception": 0}

for joueur in liste_joueur:
    if joueur.num <= 10:
        team_stats = team1_stats
    else:
        team_stats = team2_stats
    
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

stat1,stat2 = recup_stat()
afficher_stat(stat1,stat2)

#Created by Mycode Developpement