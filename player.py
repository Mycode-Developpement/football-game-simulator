import random 
from colorama import Fore
from create_player import Create_player

class Player ():
    
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
        
        
        # stat pour ceux du match en particulier 
        
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
        
        #position des joueurs 
        self.attaque1 = [8,9,10,]
        self.attaque2 = [19,20,21]
        self.milieux1 = [5,6,7]
        self.milieux2 = [16,17,18]
        self.defenseur1 = [1,2,3,4]
        self.defenseur2 = [12,13,14,15]
        
        self.minute = 0
        self.liste_joueur = Create_player()

        
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
        #self.minute = int(temps)
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
            note_defense = self.liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
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
                self.liste_joueur[self.action].Interception_reussi() #+1
                #print( Fore.LIGHTBLUE_EX + self.nom + " réussi sa passe mais "+ liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
    
        return self.action
    
    
    
    def Tir_dans_la_surface(self):
   
        random_note = random.randint(0,130)
        self.nombre_tir += 1 
        #self.minute = int(temps)
        
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
                note_arret_gardien = self.liste_joueur[11].Return_note_arret_gardien()
                num_gardien = 11
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = self.liste_joueur[0].Return_note_arret_gardien()
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
                self.liste_joueur[self.action].Arret_gardien() #+1 arret
                
 
        return self.action
    
    
    def Tir_hors_surface(self):
  
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
                note_arret_gardien = self.liste_joueur[11].Return_note_arret_gardien()
                num_gardien = 11
                
                engagement = 21 #valeur pour savoir si il y a but a qui est l'engegement
            else:
                note_arret_gardien = self.liste_joueur[0].Return_note_arret_gardien() + random.randint(0,6)
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
                self.liste_joueur[self.action].Arret_gardien()
          
        return self.action
    
    
    def Centre(self):
        #centre des latéraux ! 
       
        
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
            note_defense = self.liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
            random_note = random.randint(0,160)
            
            if random_note > note_defense:
                print( Fore.YELLOW + self.nom + " réussi son centre vers " + self.liste_joueur[self.action].Return_nom()  + " ("+ str(self.minute) + "min) "+ Fore.RESET)
                self.centre_reussi += 1 
                return self.liste_joueur[self.action].Tir_dans_la_surface() #il tir obligatoirement car le defenseur ne la touche pas 


            else:#le defenseur la coupe 
                self.action = adversaire
                
                print( Fore.YELLOW + self.nom + " réussi son centre mais "+ self.liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! (" + str(self.minute) + "min) "+ Fore.RESET)
                
                self.centre_rate += 1
                self.liste_joueur[self.action].Interception_reussi()
    
        return self.action
    
    def Passe_courte(self):
      
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
            note_defense = self.liste_joueur[adversaire].Return_note_interception() #recup note interception du defesneur choisie 
            
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
                
                self.liste_joueur[self.action].Interception_reussi()
                #print( Fore.CYAN + self.nom + " réussi son degagement mais "+ liste_joueur[int(self.action)].Return_nom() + " l'intercepte ! "+ Fore.RESET)
             
        
        return self.action 
    
    
    def Duel(self):


        
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
        note_defense_adversaire = self.liste_joueur[adversaire].Return_note_defense()
        note_attaque = self.dribble + random.randint(0,5)
        note_defense_adversaire += random.randint(0,5)
        
        if note_attaque >= note_defense_adversaire:
            #dribble réussi
            self.action = self.num
            
            self.duel_gagne += 1 
            
            self.liste_joueur[adversaire].Duel_perdu()
            if random.randint(1,5) == 2:
                print(self.nom + " a gagné son duel face à " + self.liste_joueur[adversaire].Return_nom() + " grâce a un super geste technique ! (" + str(self.minute)+ "min) ")
        else:
            self.action = adversaire
            self.duel_perdu += 1
            self.liste_joueur[self.action].Duel_gagner()
            if random.randint(1,5) == 2:
                print(self.nom + " a perdu son duel face à " + self.liste_joueur[adversaire].Return_nom() + " (" + str(self.minute) + "min) " )
        

        return self.action


