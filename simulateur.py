#projet de simulation de match football 
import random
from colorama import Fore
import time
import os 



class Joueur ():
    
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
        
        
        self.attaque1 = [8,9,10,]
        self.attaque2 = [19,20,21]
        self.milieux1 = [5,6,7]
        self.milieux2 = [16,17,18]
        self.defenseur1 = [1,2,3,4]
        self.defenseur2 = [12,13,14,15]
        
        self.minute = 0
        
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



liste_joueur = []
#création des joueur 
#Il faut modifier juste ici : 
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

team1, team2 = "PSG", "Juventus"


os.system('cls') #on efface la console 
temps = 0 #minutes depuis le début de la rencontre 



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

num = 0

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
