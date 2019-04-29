from octogone.tools import *
from octogone.strategies import *


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Shoot())
#team1.add("Dembele", Attaquant())
#team1.add("Varane", Defenseur())
#team1.add("Umtiti", Defenseur())


#team2.add("Kane", Attaquant())
#team2.add("Sterling", Attaquant())
#team2.add("Stones", Defenseur())
#team2.add("Rose", Defenseur())
 
#Static strategy

# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

"""Attaquant
    - s'il a la balle
        - se trouve dans la zone pres du goal
            -> shoot
        - ne se trouve pas dans la zone pres du goal
            - s'il peut faire la passe
                -> fais la passe à son coequipier
            - sinon
                -> avance vers la zone du goal avec la balle
    - si l'autre attaquant a la balle
        -> avance vers le goal aussi
    - s'ils n'ont pas la balle
        -> un court vers la balle, l'autre avance doucement vers goal
//Quand est ce qu'on fait une passe ?
    on fait une passe lorsque un joueur adverse se trouve dans la trajectoire entre le goal et le joueur, lorsque lequipier est assez loin et on fait une passe à l'equipier le plus proche. on ne fait pas de passe lorsqu'un dversaire se trouve entre nous et notre équipier.

Defenseur
    - s'il a la balle :
        - s'il peut la passer
            -> passe a un equipier
        - s'il ne peut pas
            -> avance vers son goal
    - si son coequipier a la balle
        -> se met entre l'adversaire le plus proche et le coequipier
    - s'ils n'ont pas la balle
        -> on se met toujours entre les joueurs (dont celui qui a la balle) et on tacle"""
    
        
    