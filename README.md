<div align="center">

# FOOTBALL GAME SIMULATOR : ⚽

**Relive the world's greatest soccer posters or those from your favorite teams.**

This is a football match simulator where 11 players on each team play against each other. The simulator is currently in beta version!

![IMAGE FOOTBALL GAME SIMULATOR](./image/@Mycode-developpement.png)

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
    "halfTime" : 45,
    "timeDisplay" : 0.01
}
```


| Key  | Value |
| ------------- | ------------- |
| ``langage``  | France : ``fr``  / English : ``en``  / spanish : ``es``  / German : ``de``  |
| ``timeGame``  | This parameter corresponds to the match time [value] : **integer** |
| ``timePerAction``  | This parameter will change the number of actions per match: the lower the number, the more actions there will be in the match.  [value] : **integer or float** |
| ``halfTime``  | This parameter corresponds to the half-time of the match [value] : **integer** |
| ``timeDisplay``  | For an action-by-action display of the match [value] : **integer or float** / 0 : instant / 1 : very long |

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

Example action according to your language :

```

Vinícius shot inside the penalty area, but the goalkeeper stopped it. (43 min)

Mendès won his duel against Vinícius with a superb technical move ! (44 min)
The referee blows the halftime whistle!
The match resumes and the ball is with Neymar
Vinícius won his duel against Ramos with a superb technical move ! (51 min)
Neymar crosses successfully to Messi(52 min)

Messi shot inside the penalty area and scored!!! Goal!! (52 min)

Neymar crosses successfully but Carvajal intercepts (52 min)
Mendès won his duel against Rodrygo with a superb technical move ! (54 min)
Mendès crosses successfully but Nacho intercepts (54 min)
Neymar shot from outside the penalty area, but the goalkeeper stopped it. (60 min)

```

End-of-match statistics :

```
+--------------------------+-------------+---------------------+
|         Category         |     PSG     |     Real Madrid     |
+--------------------------+-------------+---------------------+
|           Goal           |      2      |          0          |
|           Shot           |      13     |          6          |
|      Shot on target      |      8      |          2          |
|     Successful pass      |     267     |         361         |
|       Missed pass        |      38     |          44         |
|     Successful cross     |      5      |          1          |
|       Missed cross       |      4      |          1          |
|         Duel won         |      23     |          37         |
|        Duel lost         |      37     |          23         |
|           Save           |      2      |          6          |
|       Interception       |      1      |          8          |
+--------------------------+-------------+---------------------+
```

## Contact Me : 

- My youtube chanel : [HERE](https://www.youtube.com/@mycode-developpement)
- My e-mail address : **mycode.developpement@gmail.com**

## Licence 

**LICENCE MIT @copyright 2023 Mycode Developpement**



