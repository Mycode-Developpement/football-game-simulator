import os

def Clear():
    """Fonction qui nettoye la console"""
    if os.name == 'nt': # si le système d'exploitation est Windows
        os.system('cls') # effacer la console
    else: # sinon
        os.system('clear') # effacer la console


def write_dispo(nameTeam, dispo, color):
    max_width = 75
    formatted_text = ""
    
    print(f"{color}Composition {nameTeam} :")

    for element in dispo:
        line = "        ".join(element)
        indentation = (max_width - len(line)) // 2
        formatted_text += " " * indentation + line + "\n\n"
    
    print(formatted_text)