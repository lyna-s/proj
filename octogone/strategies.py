# coding: utf-8
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import *
from .tools import *


class Shoot(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Shoot")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        return s.shoot_or_go



"""class Attaquant(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquant")
    
    def compute_strategy(self, state, id_team, id_player):
        s=SuperState(self, state, id_team, id_player)
        if s.player == s.qui_a_la_balle :
            if s.passe_possible :
                return s.passe
            else :
                return s.petit_shoot"""
            



class Attaquant(Strategy):
    def __init__(self):
        Joueur.init__(self, "Attaquant")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(self,state,id_team, id_player)
        if s.a_la_balle :
            if s.passe_possible :
                return s.passe
            else :
                return s.avance
        else :
            return s.run
            
    
        
        
   
class Attaquanttlp(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaquanttlp")
        
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        if (s.player.distance(s.goal) < s.player.distance(s.eq_proche)):
            return s.shoot_and_go
        else :
            return s.passe   
        
class  Shoot_Anticipe(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Shoot_Anticipe")
               
    def compute_strategy(self, state, id_team, id_player):
        # id_team is 1 or 2
        # id_player starts at 0
        s = SuperState(state, id_team, id_player)
        if s.passe_possible :
            return s.passe
        else :
            return s.shoot_or_go_anticipe

   
class Dribbler (Strategy):
    def __init__(self):
        Strategy.__init__(self, "Dribbler")
        
    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state, id_team, id_player)
        if (s.adv_proche.distance(s.player) < 1):    
            if (s.can_shoot):
                return SoccerAction(Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT),Vector2D(-GAME_WIDTH/2,GAME_GOAL_HEIGHT))
            if (s.ball.x < 3*GAME_WIDTH/4):
                return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2)-s.ball/GAME_WIDTH)
            return SoccerAction(Vector2D(GAME_WIDTH,GAME_HEIGHT/2))
        
        return s.petit_shoot_or_go
       
        
  
    
class Defenseur(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Defenseur")

    def compute_strategy(self, state, id_team, id_player):
        s = SuperState(state,id_team,id_player)
        if s.nb_players == 2:
            return s.defenseur_2
        if s.nb_players == 4 :
            return s.defenseur_4

