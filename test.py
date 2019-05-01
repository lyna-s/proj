from octogone.tools import *
from octogone.strategies import *


# Create teams
team1 = SoccerTeam(name="Team 1")
team2 = SoccerTeam(name="Team 2")

# Add players
team1.add("Mbappe", Dribbleur())
#team2.add("Kane", Dribbleur())


# Create a match
simu = Simulation(team1, team2)

# Simulate and display the match
show_simu(simu)