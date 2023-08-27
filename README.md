<div align="center">

# FOOTBALL GAME SIMULATOR : ⚽

**Relive the world's greatest soccer posters or those from your favorite teams.**

This is a football match simulator where 11 players on each team play against each other. The simulator is currently in beta version! The comments and sentences in the game are written in French.

</div>

***

<details >

<summary> <h2> Summary </h2>  </summary>

- coming soon

</details>

***

## Dependencies

List of modules or dependencies used by this program :

- **colorama**
- **random**
- **os**
- **json**
- **prettytable**

## Installation

Use this command to clone the repository from GitHub : 
    
    git clone https://github.com/Mycode-Developpement/football-game-simulator.git

The easiest way to install the latest version from PyPI is by using [pip](https://pip.pypa.io/)

if a module is not installed on your machine :

    pip install [name]

## How to start the program

Run the main.py program in the code folder :

    cd code
    python main.py

## Documentation :

You can customize your gaming experience by changing these settings :

``settings.json``

``` json
 {
    "langage" : "fr", 
    "timeGame" : 90, 
    "timePerAction" : 0.09,
    "halfTime" : 45
}
```


| Key  | Value |
| ------------- | ------------- |
| ``langage``  | unavailable  |
| ``timeGame``  | This parameter corresponds to the match time [value] : **integer** |
| ``timePerAction``  | This parameter will change the number of actions per match: the lower the number, the more actions there will be in the match.  [value] : **integer or float** |
| ``halfTime``  | This parameter corresponds to the half-time of the match [value] : **integer** |

You can also change the players on the pitch :

``team1.json and team2.json``

``` json
{
    "name": "PSG"
}
```

``` json
{
    "name": "Mbappé",
    "position": "BU",
    "number": 9,
    "pass": 85,
    "shot": 90,
    "goalkeeper": 0,
    "center": 80,
    "dribble": 93,
    "defense": 30,
    "interceptions": 38

}
```

| Key  | Value |
| ------------- | ------------- |
| ``name``  | Team name [value] : **string**  |
| ``position``  | The player's position [value] : **string** |
| ``number``  | The number player  [value] : **integer** |
| ``pass``  | Player rating between 0-100 [value] : **integer** |
| ``shot``  | Player rating between 0-100 [value] : **integer** |
| ``goalkeeper``  | Player rating between 0-100 [value] : **integer** |
| ``center``  | Player rating between 0-100 [value] : **integer** |
| ``dribble``  | Player rating between 0-100 [value] : **integer** |
| ``defense``  | Player rating between 0-100 [value] : **integer** |
| ``interceptions``  | Player rating between 0-100 [value] : **integer** |

## Players Positions :

| Postions  | Explicit positions |
| ------------- | ------------- |
| ``G``  | Goalkeeper |
| ``DD``  | Right-back |
| ``DC``  | Central defender |
| ``DG``  | Left-back |
| ``MC``  | central midfielder |
| ``AD``  | Right-wing |
| ``AG``  | Right-left |
| ``AC``  | Stricker |

## Intelligent placement :

your players will automatically move to the position you've defined. The tactics are endless - it's up to you to create them! 

 

### Composition PSG :
    
                                Donnarumma

            Hakimi        Ramos        Marquinhos        Mendès

                   Veratti        Vitinha        Sanches

                     Messi        Mbappé        Neymar



### Composition Real Madrid :
                                 Courtois

             Carvajal        Rüdiger        Alaba        Nacho

       Valverde        Tchouaméni        Camavinga        Bellingham

                          Vinícius        Rodrygo

## Match day :

The most important actions of the match are displayed in the console.

Example action in french :

``` txt

Mbappé a tiré hors de la surface et a marqué !!! But !! (64min)

Mbappé a tiré en dehors de la surface et n'a pas réussi à cadré ! Balle pour le gardien adverse. (67min)
Carvajal a perdu son duel face à Ramos (69min)
Sanches a perdu son duel face à Tchouaméni (69min)
Neymar réussi son centre vers Mbappé (71min)
Mbappé a tiré dans la surface mais n'a pas réussi à cadré ! Balle pour le gardien adverse. (71min)
Alaba a gagné son duel face à Neymar grâce a un super geste technique ! (74min)
Rodrygo a tiré hors de la surface mais le gardien l'a arrêter ! (75min)

```

End-of-match statistics in French :

``` python output
+-----------------------+-------------+---------------------+
|       Catégorie       |     PSG     |     Real Madrid     |
+-----------------------+-------------+---------------------+
|          But          |      2      |          0          |
|          Tir          |      11     |          8          |
|       Tir_cadré       |      5      |          4          |
|      Passe_réussi     |     248     |         414         |
|       Passe_raté      |      43     |          45         |
|     Centre_réussi     |      4      |          1          |
|      Centre_raté      |      4      |          3          |
|       Duel_gagné      |      19     |          18         |
|       Duel_perdu      |      18     |          19         |
|         Arrêt         |      4      |          3          |
|      Interception     |      3      |          6          |
+-----------------------+-------------+---------------------+
```

## Contact Me : 

- My youtube chanel : [HERE](https://www.youtube.com/@mycode-developpement)
- My e-mail address : **mycode.developpement@gmail.com**

## Licence 

**LICENCE MIT @copyright 2023**



