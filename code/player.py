import random
from colorama import Fore

class Joueur ():
    """Class Joueur : permet de créer les joueurs des deux équipes numéroté id entre 0 et 21"""    
    def __init__(self, nom, poste, num, passe, tir, arret, centre, dribble, defense, interception, adversary, color1, color2, dispo, dispo_adversary, text):
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
        self.color1 = color1
        self.color2 = color2
        
        self.adversary = adversary #the opponents with whom the player will have most of these duels (the same positions)
        self.dispo = dispo
        self.dispo_adversary = dispo_adversary
        
        self.text = text
        
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
        
        self.minute = "(0min)"
    
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
        
    def Random_Action (self,temps, list_player):
        """Fonction principale appelé lors de chaque action : 
        - Aucun paramatre en entré
        - En sortie le numéro du joueur qui a maintenant la balle 
        Cette fonction varie selon le poste du joueur. 
        """
        self.minute = int(temps)
        self.minute = f"({self.minute} min)"
        self.list_player = list_player
        
        #code executé quand le joueur recoit le ballon
        if self.poste == "AC":
            random_action = random.randint(0,42)
            if random_action == 1:
                #tir dans la surface 
                return self.Tir_dans_la_surface(self.list_player)
            
            elif random_action == 2:
                return self.Tir_hors_surface()
            
            elif random_action == 3 or random_action == 4:
                return self.Passe_courte()
            
            elif random_action <= 7:
                return self.Duel()
            
            else: #passe
                return self.Passe()
        
        
        elif self.poste == "AG" or self.poste == "AD":
            random_action = random.randint(0,55)
            if random_action == 2:
                #tir dans la surface 
                return self.Tir_dans_la_surface(self.list_player)
            
            elif random_action <= 4:
                return self.Tir_hors_surface()
            
            elif random_action <= 8:
                return self.Centre()
            
            elif random_action <= 13:
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
            random_action = random.randint(0,40)
            
            if random_action == 1:
                return self.Centre()
            
            elif random_action <= 15:
                return self.Passe_courte()
            
            elif random_action <= 18:
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
            
            defenseur = self.adversary
            
            #choisir l'adversaire qui peut couper le centre 
            adversaire = random.choice(defenseur)
            note_defense = self.list_player[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
            random_note = random.randint(0,5000)
            
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
                #print(self.nom + " a réussi sa passe en direction de " + self.list_player[self.action].Return_nom())


            else:
                #le defenseur la coupe 
                self.action = adversaire
                self.passe_rate += 1
                self.list_player[self.action].Interception_reussi() #+1
                #print( Fore.LIGHTBLUE_EX + self.nom + " réussi sa passe mais "+ self.list_player[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
    
        return self.action
    
    
    
    def Tir_dans_la_surface(self, list_player):
        self.list_player = list_player
        
        random_note = random.randint(0,140)
        self.nombre_tir += 1      
        if random_note > self.tir : 
            #le tir est raté
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
                # On rend la balle au gardien 
            print (self.color1 + self.nom + self.text[0][0] + self.minute + Fore.RESET)
            ##print (self.color1 +self.nom + " a tiré dans la surface mais n'a pas réussi à cadré ! Balle pour le gardien adverse. (" + str(self.minute) + "min) " + Fore.RESET)
            
        
        else:
    
            #le tir est cadré 
            #il faut verifier si le gardien adverse arrive a faire l'arrêt ou pas         
            if self.num <= 10:
                #le gardien adverse est donc le numéro 11
                
                note_arret_gardien = self.list_player[11].Return_note_arret_gardien()
                num_gardien = 11
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = self.list_player[0].Return_note_arret_gardien()
                num_gardien = 0
                engagement = 11
            
            random_note = random.randint(0,130) #savoir si le gardien l'arrête
            
            if random_note > note_arret_gardien:
                #il y a donc but dans la surface 
                print("")
                print(self.color2 + self.nom + self.text[1][0] + self.minute + Fore.RESET + "\n")
                ##print(self.color2 + self.nom + " a tiré dans la surface et a marqué !!! But !! ("  + str(self.minute) + "min) ")
                ##print(Fore.RESET + "\n")
                self.action = engagement
                self.nombre_but += 1
                self.nombre_tir_cadre += 1
               

            else:
                #le gardien l'arrete, il garde la balle 
                self.action = num_gardien
                print(self.color1 + self.nom + self.text[2][0] + self.minute + Fore.RESET + "\n")
                ##print(self.color1 + self.nom + " a tiré dans la surface surface mais le gardien l'a arrêter ! (" + str(self.minute) + "min) ")
                ##print(Fore.RESET + "\n")
                self.nombre_tir_cadre += 1
                self.list_player[self.action].Arret_gardien() #+1 arret
 
        return self.action
    
    
    def Tir_hors_surface(self):
 
        random_note = random.randint(0,160) 
        self.nombre_tir += 1
        
        if random_note > self.tir : 
            #le tir est raté
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
                # On rend la balle au gardien 
            print(self.color1 + self.nom + self.text[3][0] + self.minute + Fore.RESET + "\n")
            #print (self.color1 + self.nom + " a tiré en dehors de la surface et n'a pas réussi à cadré ! Balle pour le gardien adverse. ("  + str(self.minute) + "min) ")
        
        
        else:
            #le tir est cadré 
            #il faut verifier si le gardien adverse arrive a faire l'arrêt ou pas         
            if self.num <= 10:
                #le gardien adverse est donc le numéro 11
                note_arret_gardien = self.list_player[11].Return_note_arret_gardien()
                num_gardien = 11
                
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = self.list_player[0].Return_note_arret_gardien() + random.randint(0,6)
                num_gardien = 0
                engagement = 11
            
            random_note = random.randint(0,100) #savoir si le gardien l'arrête
            
            if random_note > note_arret_gardien:
                #il y a donc but 
                print("\n" +self.color2 + self.nom + self.text[4][0] + self.minute + Fore.RESET + "\n")
                ##print(self.color2 + self.nom + " a tiré hors de la surface et a marqué !!! But !! ("  + str(self.minute) + "min) ")
                ##print(Fore.RESET + "\n")
                self.action = engagement
                self.nombre_but += 1
                self.nombre_tir_cadre += 1
             

            else:
                #le gardien l'arrete, il garde la balle 
                self.action = num_gardien
                print(self.color1 + self.nom + self.text[5][0] + self.minute + Fore.RESET + "\n")
                ##print(self.color1 + self.nom + " a tiré hors de la surface mais le gardien l'a arrêter ! ("  + str(self.minute) + "min) ")
                self.nombre_tir_cadre += 1
                self.list_player[self.action].Arret_gardien()
          
        return self.action
    
    
    def Centre(self):
        #centre des latéraux ! 

        random_note = random.randint(0,75)
        
        if random_note > self.centre:
            # sors en 6 mètre 
            if self.num <= 10:
                self.action = 11
            else:
                self.action = 0
            
            print(self.color1 + self.nom + self.text[6][0] + self.minute + Fore.RESET + "\n")
            ##print(Fore.RED+ self.nom + " a raté son centre qui file en sorti de but (" + str(self.minute) + "min) " + Fore.RESET)
            
            self.centre_rate += 1

        else:
            #centre réussi
            self.action = self.num
            if len(self.dispo[-1]) >= 2:  
                while self.action == self.num:
                    self.action = random.choice(self.dispo[-1])
            else:
                while self.action == self.num:
                    #print(Fore.RED+ "Pas assez d'attaquants !"+ Fore.RESET)
                    playerListAction = self.dispo[-1] + self.dispo[-2]
                    self.action = random.choice(playerListAction)
                    
            #maintenant il faut verifier si ce n'est pas intercepté
            
            defenseur = random.choice(self.dispo_adversary[1])
            note_defense = self.list_player[defenseur].Return_note_interception() + (len(self.dispo_adversary[1])*3) #recup note interception du defenseur choisie 
            
            random_note = random.randint(0,160)
            
            if random_note > note_defense:
                print(self.color1 + self.nom + self.text[7][0] + self.list_player[self.action].Return_nom() + self.minute + Fore.RESET)
                ##print( self.color1 + self.nom + " réussi son centre vers " + self.list_player[self.action].Return_nom()  + " ("+ str(self.minute) + "min) "+ Fore.RESET)
                self.centre_reussi += 1 
                return self.list_player[self.action].Tir_dans_la_surface(self.list_player) #il tir obligatoirement car le defenseur ne la touche pas 


            else:#le defenseur la coupe 
                self.action = defenseur
                print(self.color1 + self.nom + self.text[8][0][0] + self.list_player[int(self.action)].Return_nom()+ self.text[8][1][0] + self.minute + Fore.RESET)
                ##print( self.color1 + self.nom + " réussi son centre mais "+ self.list_player[int(self.action)].Return_nom() + " l'intercepte ! (" + str(self.minute) + "min) "+ Fore.RESET)
                
                self.centre_rate += 1
                self.list_player[self.action].Interception_reussi()
    
        return self.action
    
    def Passe_courte(self):

        random_note = random.randint(0,95)  #note aléatoire qui permet de savoir si un geste est réussi
        
        if random_note > self.passe:
            #passe raté
            self.action = random.choice(self.adversary)
            
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
                    
            #print(self.nom + " a réussi sa passe courte vers " + self.list_player[self.action].Return_nom())
            self.passe += 1
        
        return self.action
    
    
    def Degagement(self):

        random_note = random.randint(0,130)  #note aléatoire qui permet de savoir si un geste est réussi
        
        if random_note > self.passe:
            #degagement raté
            if self.num <= 10:   
                self.action = random.randint(12,18)
            else:
                self.action = random.randint(1,7)
            
            #print(self.nom + " a raté son degagement, recupération :  " + self.list_player[self.action].Return_nom() ) 
            
        
        else:
            
            #maintenant il faut verifier si ce n'est pas intercepté
            
            defenseur = self.adversary
            
            #choisir l'adversaire qui peut couper le centre 
            adversaire = random.choice(defenseur)
            note_defense = self.list_player[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
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
                
                #print(self.nom + " a réussi son degagement vers :  " + self.list_player[self.action].Return_nom() )   
                
           
            else: #le defenseur l'intercepte 
                self.action = adversaire
                
                self.list_player[self.action].Interception_reussi()
                #print( Fore.CYAN + self.nom + " réussi son degagement mais "+ self.list_player[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
             
        
        return self.action 
    
    
    def Duel(self):
        #defense par zone 
        random_ = random.randint(0,5)
        if random_ == 2:
            if self.num <= 10:  
                adversaire = random.randint(12,21)
            else:
                adversaire = random.randint(1,10)
        else:
            adversaire = random.choice(self.adversary)
        
        #on a maintenant l'adversaire 
        note_defense_adversaire = self.list_player[adversaire].Return_note_defense()
        note_attaque = self.dribble + random.randint(0,5)
        note_defense_adversaire += random.randint(0,5)
        
        if note_attaque >= note_defense_adversaire:
            #dribble réussi
            self.action = self.num
            
            self.duel_gagne += 1 
            
            self.list_player[adversaire].Duel_perdu()
            if random.randint(1,5) == 2:
                print(self.nom + self.text[9][0][0] + self.list_player[adversaire].Return_nom() + self.text[9][1][0] + self.minute)
                ##print(self.nom + " a gagné son duel face à " + self.list_player[adversaire].Return_nom() + " grâce a un super geste technique ! (" + str(self.minute)+ "min) ")
        else:
            #lose this duel 
            self.action = adversaire
            self.duel_perdu += 1
            self.list_player[self.action].Duel_gagner()
            if random.randint(1,5) == 2:
                print(self.nom + self.text[10][0] + self.list_player[adversaire].Return_nom() + self.minute)
                ##print(self.nom + " a perdu son duel face à " + self.list_player[adversaire].Return_nom() + " (" + str(self.minute) + "min) " )
        

        return self.action