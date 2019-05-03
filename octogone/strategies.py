# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from .tools import *



class ExFonceur(Strategy):
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
        
"""class Fonceur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.to_goal_anticipe()"""

class Fonceur (Strategy):
    def __init__(self):
        Strategy.__init__(self, "Fonceur")
        
    def compute_strategy(self, state, id_team, id_player):
        #id_team is 1 or 2
        #id_player starts at 0
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        #if s.ball.x != GAME_WIDTH/2 and s.ball.y != GAME_HEIGHT/2 :
        return move.to_ball()+shoot.to_goal()

    
class Dribbleur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbleur")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.to_ball() + shoot.dribble()
    
class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        move = Move(s)
        shoot = Shoot(s)
        return move.passe()
        
        """if (s.zone_tir == True):
            return move.to_ball()+shoot.dribble()
        else :
            if s.passe_possible :
                return shoot.passe()
            else :
                if (self.id_team == 1):
                    return move.to_ball()+shoot.dribble()
                if (self.id_team == 2):
                    return move.avance()"""
            


          
        
"""def gobetter(state) :
    if state.player.distance(state.ball)<PLAYER_RADIUS+BALL_RADIUS :
            return SoccerAction(shoot = state.goal-state.player)
    else :
            return SoccerAction(acceleration=state.ball-state.player)"""

            
        

            

 