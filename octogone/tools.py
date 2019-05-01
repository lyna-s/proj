# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction
from soccersimulator.settings import *

class SuperState():
    def __init__(self,state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        
    def __getattr__ (self , attr):
        return getattr (self.state , attr)
       
	#position du goal
    @property
    def goal(self):
        if (self.id_team==1):
            return Vector2D(GAME_WIDTH,GAME_HEIGHT /2)
        else :
            return Vector2D(0, GAME_HEIGHT/2)
        
	#position du joueur
    @property
    def player(self):
        return self.state.player_state(self.id_team,self.id_player).position
   
    #positon de la balle     
    @property
    def ball(self):
        return self.state.ball.position