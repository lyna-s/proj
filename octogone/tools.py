# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction, Strategy
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
    
   #position de l'autre joueur
    @property
    def player_pos(self, numero):
        if numero == 2 :
            return self.state.player_state(self.id_team, 2).position
        if numero == 3 :
            return self.state.player_state(self.id_team, 3).position
        if numero == 4 :
            return self.state.player_state(self.id_team, 4).position
   
    #positon de la balle     
    @property
    def ball(self):
        return self.state.ball.position
    
    #anticiper la position de la balle
    @property
    def ball_anticipe(self):
        return self.state.ball.position+self.player.distance(self.ball)*self.state.ball.vitesse
    
    #donne la position d'un joueur donné
    @property
    def adversaire_proche(self):
        opponents = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if (id_team!=self.id_team)]
        return min ([(self.player.distance(player), player) for player in opponents])[1]
    
    #donne la position de l'équipier proche
    @property
    def equipier_proche(self):
        equipiers = [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if (id_team==self.id_team)]
        return min ([(self.player.distance(player), player) for player in equipiers])[1]
    
    #pose les conditions d'une passe 
    @property
    def passe_possible(self):
        if (self.equipier_proche.distance(self.player)<self.player.distance(self.goal) and (self.equipier_proche.distance(self.player))>30):
            if ((self.adversaire_proche-self.player) * (self.goal - self.player) == 0):
                return True
        return False
    
    #retourne True si on se trouve dans la zone de tir, False sinon
    @property
    def zone_tir(self):
        if (self.id_team == 1):
            if (self.player.x > 3*GAME_WIDTH/4) and (self.player.y > GAME_HEIGHT/3) and (self.player.y < 2*GAME_HEIGHT/3):
                return True
            return False
        if (self.id_team ==2):
            if (self.player.x < GAME_WIDTH/4) and (self.player.y > GAME_HEIGHT/3) and (self.player.y < 2*GAME_HEIGHT/3):
                return True
            return False
        
    

"""class SimpleStrategy (Strategy):
    def __init__ (self, action, name):
        super().__init__(name)
        self.action = action

    def compute_strategy (self, state ,id_team ,id_player):
        s = SuperState (state, id_team, id_player)
        return self.action(s)  """




class Move(): 
    def __init__(self, superstate):
        self.superstate = superstate
    
    def move(self, acceleration=None):
        return SoccerAction(acceleration=acceleration)
    
    #court vers la balle
    def to_ball(self):
        return self.move(self.superstate.ball-self.superstate.player)
    
    def avance (self):
        return self.move(self.superstate.goal-self.superstate.player)

    def passe (self):
        return self.move(self.superstate.equipier_proche-self.superstate.player)
    
    
    
class Shoot():
    def __init__(self, superstate):
        self.superstate = superstate
        
    def shoot(self, direction=None):
            dist = self.superstate.player.distance(self.superstate.ball)
            if dist < PLAYER_RADIUS + BALL_RADIUS:
                return SoccerAction(shoot=direction)
            else:
                return SoccerAction()

    def to_goal(self, strength=None):
        return self.shoot((self.superstate.goal-self.superstate.player)*maxPlayerShoot)
    
    def dribble(self, strength=None):
        return self.shoot((self.superstate.goal-self.superstate.player)*maxPlayerAcceleration/10)
    
    def passe(self, strength=None):
        return self.shoot((self.superstate.equipier_proche-self.superstate.player)*maxPlayerShoot)

    