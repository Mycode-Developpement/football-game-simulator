from player import Joueur

def create_player():  
    """Fonction création de joueur appelé au démarage. C'est ici qu'il faut faire les modifications d'équipe"""
    list_player = []
    list_player.append(Joueur("Donnarumma", "G",0,56,0,90,0,0,0,0,))
    list_player.append(Joueur("Hakimi", "DD", 1, 81, 68, 0, 77, 79,76,78))
    list_player.append(Joueur("Ramos", "DC", 2,78, 0,0,0,63,83,84))
    list_player.append(Joueur("Marquinhos", "DC", 3,84, 0,0,0,69,89,89))
    list_player.append(Joueur("Mendès", "DG", 4,77,0,0,66,77,75,74))
    list_player.append(Joueur("Veratti", "MC", 5,90,58,0,0,91,80,85))
    list_player.append(Joueur("Vitinha", "MC", 6,85,71,0,0,82,70,73))
    list_player.append(Joueur("Sanches", "MC", 7,81,78,0,0,84,70,75))
    list_player.append(Joueur("Messi", "AD", 8,91,90,0,87,95,32,34))
    list_player.append(Joueur("Mbappé", "BU",9,85,90,0,80,93,30,38))
    list_player.append(Joueur("Neymar", "AG",10,85,83,0,80,95,30,37))

    list_player.append(Joueur("Szczęsny", "G", 11,56,0,86,0,0,0,0))
    list_player.append(Joueur("Cuadrado", "DD", 12,81,65,0,84,90,80,73))
    list_player.append(Joueur("Bonucci", "DC", 13,81,0,0,0,69,82,86))
    list_player.append(Joueur("Bremer", "DC", 14,69,0,0,0,62,84,84))
    list_player.append(Joueur("Alex Sandro", "DG", 15,75,0,0,82,78,78,75))
    list_player.append(Joueur("Locatelli", "MC", 16,85,80,0,0,78,77,79))
    list_player.append(Joueur("McKennie", "MC", 17,79,73,0,0,81,79,79))
    list_player.append(Joueur("Zakaria", "MC", 18,79, 63,0,0,78,80,80))
    list_player.append(Joueur("Di María", "AD", 19,82,82,0,85,88,53,42))
    list_player.append(Joueur("Vlahović", "BU",20,73, 88, 0,57,80,25,25))
    list_player.append(Joueur("Kean", "AG",21,68,79,0,48,79,30,31))
    return list_player
