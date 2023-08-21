import os

def Clear():
    """Fonction qui nettoye la console"""
    if os.name == 'nt': # si le système d'exploitation est Windows
        os.system('cls') # effacer la console
    else: # sinon
        os.system('clear') # effacer la console
        
