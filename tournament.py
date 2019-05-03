#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from octogone import *
from soccersimulator import show_simu, Simulation

  
#Check team with 1 player and 2 players
team1=get_team(1)
team2=get_team(2)
    
#Create a match
simu = Simulation(team1, team2)
#simulate and display the match
show_simu(simu)    
