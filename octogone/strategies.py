# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from .tools import SuperState
from .action import Move, Shoot



class Fisrt_Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Shoot")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        if s.player.distance(s.ball)<PLAYER_RADIUS+BALL_RADIUS :
            return SoccerAction(shoot = s.goal-s.player)
        else :
            return SoccerAction(acceleration=s.ball-s.player)
        
class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.to_goal()
    
class Dribbleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbleur")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        
        return move.to_ball() + shoot.dribble()


            

 