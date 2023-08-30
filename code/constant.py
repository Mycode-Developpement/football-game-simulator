import json


def get_const_json(path):
    with open(path, "r", encoding='utf-8') as json_file:
        data = json.load(json_file) 
    return data


variable = get_const_json("../Settings/settings.json")

GAME_TIME = variable['timeGame']  
TIME_PER_ACTION = variable['timePerAction']    
HALF_TIME = variable['halfTime']  
LANGUAGE = variable['langage']
TIME_DISPLAY = variable['timeDisplay']


variable = get_const_json("../Settings/team1.json")
variable2 = get_const_json("../Settings/team2.json")

NAME_TEAM = [variable['name'], variable2['name']]



TEXT_LANGUAGE = {
    "fr": [
        [" tire dans la surface de réparation mais n'a pas réussi à trouver le cadre ! Balle pour le gardien adverse. "],
        [" tire dans la surface de réparation et marque ! But !!! "], 
        [" tire dans la surface de réparation, mais le gardien arrête le tir. "], 
        [" tire de l'extérieur de la surface de réparation mais n'a pas pu atteindre la cible ! Le ballon revient au gardien de but adverse. "], 
        [" tire de l'extérieur de la surface de réparation et marque ! But !!! "], 
        [" tire de l'extérieur de la surface de réparation, mais le gardien arrête le tir."],
        [" manque son centre et le ballon sort pour un coup de pied arrêté. "],
        [" réussi son centre vers "],
        [[" réussi son centre mais "],[" l'intercepte "]],
        [[" a remporté son duel contre "],[" grâce à un superbe geste technique !"]], 
        [" a perdu son duel face à "], 
        ["L'arbitre fait le tirage au sort pour le ballon : l'engagement est donc pour "], 
        ["L'arbitre sifle la mi-temps !"], 
        ["Le Match reprend et la balle et pour "],
        ["Le match est terminé !!"], 
        
        #stat
        [
            "Composition", "Catégorie", "But", "Tir", "Tir_cadré", "Passe_réussi", "Passe_raté", "Centre_réussi", "Centre_raté", "Duel_gagné", "Duel_perdu", "Arrêt", "Interception"
        ]
        
    ],
    
    "en": [
        [" shot inside the penalty area but failed to hit the target! Ball goes to the opposing goalkeeper. "],
        [" shot inside the penalty area and scored!!! Goal!! "], 
        [" shot inside the penalty area, but the goalkeeper stopped it. "], 
        [" shot from outside the penalty area and couldn't hit the target! Ball goes to the opposing goalkeeper. "],
        [" shot from outside the penalty area and scored ! Goal !!! "], 
        [" shot from outside the penalty area, but the goalkeeper stopped it. "], 
        [" missed his cross, and the ball goes out for a goal kick. "],
        [" crosses successfully to "],
        [[" crosses successfully but "],[" intercepts "]],
        [[" won his duel against "], [" with a superb technical move ! "]], 
        [" lost his duel against "],
        ["The referee tosses the coin for the ball: the kick-off is for "],
        ["The referee blows the halftime whistle!"],
        ["The match resumes and the ball is with "],
        ["The match is over!"],
        
        #stat
        [
            "Composition","Category", "Goal", "Shot", "Shot on target", "Successful pass", "Missed pass", "Successful cross", "Missed cross", "Duel won", "Duel lost", "Save", "Interception"
        ],
        
    ],
    
    "es": [
        [" disparo dentro del área penal pero no logró dar en el blanco. ¡La pelota va al portero contrario! "],
        [" disparo dentro del área penal y ¡gol! ¡¡¡Gol!!! "], 
        [" disparo dentro del área penal, pero el portero lo detuvo. "], 
        [" disparo desde fuera del área penal y no pudo dar en el blanco. ¡La pelota va al portero contrario! "],
        [" disparo desde fuera del área penal y ¡gol! ¡¡¡Gol!!! "], 
        [" disparo desde fuera del área penal, pero el portero lo detuvo. "], 
        [" falló su centro, y la pelota sale para un saque de portería. "],
        [" centra con éxito hacia "],
        [[" centra con éxito pero "],[" intercepta "]],
        [[" ganó su duelo contra "], [" con un movimiento técnico soberbio ! "]], 
        [" perdió su duelo contra "],
        ["El árbitro lanza la moneda para el balón: ¡el saque inicial es para "],
        ["¡El árbitro pita el medio tiempo!"],
        ["¡El partido continúa y el balón está con !"],
        ["¡Se acabó el partido!"],
        
        #stat
        [
            "Composición","Categoría", "Gol", "Disparo", "Disparo al arco", "Pase exitoso", "Pase fallido", "Centro exitoso", "Centro fallido", "Duelo ganado", "Duelo perdido", "Parada", "Intercepción"
        ],
    ],
    
    "de": [
        [" Schuss im Strafraum, aber das Ziel wurde verfehlt! Der Ball geht zum gegnerischen Torwart. "],
        [" Schuss im Strafraum und Tor!!! Tor!! "], 
        [" Schuss im Strafraum, aber der Torwart hat ihn gehalten. "], 
        [" Schuss von außerhalb des Strafraums, aber das Ziel wurde verfehlt! Der Ball geht zum gegnerischen Torwart. "],
        [" Schuss von außerhalb des Strafraums und Tor!!! Tor!! "], 
        [" Schuss von außerhalb des Strafraums, aber der Torwart hat ihn gehalten. "], 
        [" Fehlgeschlagene Flanke, der Ball geht ins Aus für einen Abstoß. "],
        [" Erfolgreiche Flanke zu "],
        [[" Erfolgreiche Flanke, aber "],[" abgefangen "]],
        [[" Gewinnt das Duell gegen "], [" mit einer großartigen technischen Bewegung! "]], 
        [" Verliert das Duell gegen "],
        ["Der Schiedsrichter wirft die Münze für den Ball: der Anstoß ist für "],
        ["Der Schiedsrichter pfeift zur Halbzeit!"],
        ["Das Spiel wird fortgesetzt und der Ball ist bei "],
        ["Das Spiel ist aus !!!"],
        
        #stat
        [
            "Zusammensetzung","Kategorie", "Tor", "Schuss", "Schuss auf das Tor", "Erfolgreicher Pass", "Fehlgeschlagener Pass", "Erfolgreiche Flanke", "Fehlgeschlagene Flanke", "Duell gewonnen", "Duell verloren", "Rettung", "Abfangen"
        ],
    ],
}



