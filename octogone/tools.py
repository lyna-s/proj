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
   



    

   

#POSITIONS
        
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

    
#DISTANCE

    #distance au goal
    @property
    def distance_goal(self):
        return self.goal.distance(self.player)
    
    #aller à un point donné
    def go_to_position(self, x, y):
        pos = Vector2D(x,y)
        return SoccerAction(pos-self.player)
    
#JOUEURS
    
    #retourne vrai si le joueur a la balle, faux sinon
    @property
    def has_the_ball(self):
        return self.ball.distance(self.player) < PLAYER_RADIUS+BALL_RADIUS
    
    #nombre de joueurs dans une équipe
    @property
    def nb_players(self):
        return len(self.liste_eq)  
    
    #quel équipe a le ballon
    """def team_ball(self):
       for (int i =0; i < liste_equipiers.length; i++):
           if liste_equipiers[i].has_the_ball == true:
               return 1 
       return 2"""
         
       
     #liste des adversaires
    @property
    def liste_adv(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]
    
    #liste des equipiers
    @property
    def liste_eq(self):
        return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team == self.id_team]
    
    #adversaire le plus proche    
    @property
    def adv_proche(self):
        adversaire = self.liste_adv
        return min([(self.player.distance (player), player) for player in adversaire])[1]
    
    #equipier le plus proche
    @property
    def eq_proche(self):
        equipier = self.liste_eq
        return min([(self.player.distance (player), player) for player in equipier])[1]
    
    
#ACTIONS
    
    #aller vers le ballon
    @property
    def run(self):
        return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)
    
    #avance avec le ballon
    @property    
    def avance(self):
        if (self.has_the_ball):
            return SoccerAction(shoot=0.2*((self.goal-self.player)/20))
        else:
            return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)

    #shooter dans la balle
    @property
    def shoot(self):
        return SoccerAction(shoot=((self.goal-self.player)/20)*maxPlayerShoot)

    #shooter dans la balle
    @property
    def petit_shoot(self):
        return SoccerAction(shoot=0.2*((self.goal-self.player)/20))

	#shooter dans la balle ou aller vers la balle
    @property    
    def shoot_or_go(self):
        if (self.has_the_ball):
            return self.shoot
        else:
            return self.go 
        
 
        
      #anticiper la position de la balle
    @property
    def ball_anticipe(self):
        return self.state.ball.position+self.player.distance(self.ball)*0.5*self.state.ball.vitesse
    
    #aller vers la position anticipée de la balle
    @property
    def go_anticipe (self):
        return SoccerAction((self.ball_anticipe-self.player)*maxPlayerAcceleration) 
    
    #shooter dans la balle ou aller vers la position anticipée de la balle
    @property    
    def shoot_or_go_anticipe(self):
        if (self.can_shoot):
            return self.shoot
        else:
            return self.go_anticipe
    


    #distance de l'équipier le plus proche à la balle
    @property
    def distance_eq_ball(self):
        return self.eq_proche.distance(self.ball)
    
     #distance de l'adversaire le plus proche à la balle
    @property
    def distance_adv_ball(self):
        return self.adv_proche.distance(self.ball)
    
	#faire la passe à l'équipier le plus proche
    @property
    def passe(self):
        if (self.can_shoot):
            return SoccerAction(shoot=((self.eq_proche-self.player)/20)*maxPlayerShoot)
        else:
            return SoccerAction((self.ball-self.player)*maxPlayerAcceleration)
    
    #condition pour une passe
    """@property
    def passe_possible(self):
        if ((self.adv_proche-self.player).angle == (self.eq_proche-self.player).angle :
            return False
        if (self.eq_proche.distance(self.player)<self.player.distance(self.goal) and (self.eq_proche.distance(self.player))>30):
            if ((self.adv_proche-self.player).angle == (self.goal - self.player).angle):
            return True
        else :  
            return False"""
            
    #joueur qui a la balle
    @property
    def qui_a_la_balle(self):
        joueurs = self.liste_eq+self.liste_adv
        return min([(self.ball.distance (player), player) for player in joueurs])[1]
    

    
        
   #??????????     
    @property 
    def move(self) : 
        if self.goal.distance(self.adv_proche)<20:
            return False 
        else : 
            return True

    #defenseur pour les équipes de 2 joueurs
    @property
    def defenseur_2(self): 
        pos_x = GAME_WIDTH/15
        pos_y = GAME_HEIGHT/2
        if self.id_team == 1 and self.id_player == 1:
            #si la balle se trouve dans le côté gauche
            if (self.ball.x < GAME_WIDTH/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(pos_x,(pos_y+self.ball.y)/2)
        if self.id_team == 2 and self.id_player == 1 :
            #si la balle se trouve dans le côté droit
            if (self.ball.x > GAME_WIDTH/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(14*pos_x, (pos_y+ self.ball.y)/2)
            

    
    
    #defenseur pour les équipes de 4 joueurs
    @property
    def defenseur_4(self):
        pos_x = GAME_WIDTH/15
        pos_y = GAME_HEIGHT/4
        #la balle se trouve dans le côté gauche en haut
        if self.id_team == 1 and self.id_player == 2:
            if (self.ball.x < GAME_WIDTH/2 and self.ball.y < GAME_HEIGHT/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(pos_x, pos_y)
        #la balle se trouve dans le côté gauche en bas
        if self.id_team == 1 and self.id_player == 3 :
            if (self.ball.x < GAME_WIDTH/2 and self.ball.y > GAME_HEIGHT/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(pos_x, 3*pos_y)
        #la balle se trouve dans le côté droit en haut
        if self.id_team == 2 and self.id_player == 2:
            if (self.ball.x > GAME_WIDTH/2 and self.ball.y < GAME_HEIGHT/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(14*pos_x, pos_y)
        #la balle se trouve dans le côté droit en bas
        if self.id_team == 2 and self.id_player == 3 :
            if (self.ball.x > GAME_WIDTH/2 and self.ball.y > GAME_HEIGHT/2) :
                return self.shoot_or_go_anticipe
            else :
                return self.go_to_position(14*pos_x, 3*pos_y)



    
	
