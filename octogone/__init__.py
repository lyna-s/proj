from octogone.strategies import *
from soccersimulator import SoccerTeam

def get_team(nb_players):
	team = SoccerTeam(name="Lyna et Mehdi")
	if nb_players == 1:
		team.add("Mbappe", Attaquant())
	if nb_players == 2 :
		team.add("Mbappe", Attaquant())
		team.add("Umtiti",Defenseur())
	if nb_players == 4 :
		team.add("Mbappe",Attaquant())
		team.add("Umtiti",Attaquant())
		team.add("Dembele",Defenseur())
		team.add("Varane",Defenseur())
	return team
	    
