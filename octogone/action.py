# coding: utf-8
from soccersimulator import Vector2D, MobileMixin , SoccerAction
from soccersimulator.settings import *

class Move(): 
    def __init__(self, superstate):
        self.superstate = superstate
    
    def move(self, acceleration=None):
        return SoccerAction(acceleration=acceleration)
    
    #court vers la balle
    def to_ball(self):
        return self.move(self.superstate.ball-self.superstate.player)
    
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
        return self.shoot((self.superstate.goal-self.superstate.player)*maxPlayerAcceleration)
    
    def dribble(self, strength=None):
        return self.shoot((self.superstate.goal-self.superstate.player)*maxPlayerAcceleration/10)
