import os

def Clear():
    """Fonction qui nettoye la console"""
    if os.name == 'nt': # si le système d'exploitation est Windows
        os.system('cls') # effacer la console
    else: # sinon
        os.system('clear') # effacer la console


def write_dispo(nameTeam, dispo, color, text):
    max_width = 75
    formatted_text = ""
    
    dispo_str = ""
    
    for element in dispo:
        dispo_str += str(len(element)) + "-"
        line = "        ".join(element)
        indentation = (max_width - len(line)) // 2
        formatted_text += " " * indentation + line + "\n\n"
        
    print(f"{color}{text} {nameTeam} : {dispo_str[2:-1]}")
    
    print(formatted_text)