from octogone.tools import *
from octogone.strategies import *


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Papa", Attaquant())
team1.add("Moncef", Attaquant())
#team2.add("Maman", Fonceur())


# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)

