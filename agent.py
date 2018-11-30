# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:12:36 2017

@author: david
"""

from pandas import DataFrame

class Agent:
    
    def __init__(self, name, ID, strategy, starting_score=0):#, prob_of_death = 0.015, age=0, fitness=0, actions=[]):
        self.name = name+str(ID)
        self.strategy = strategy
        self.score = starting_score # if modeling wealthb - initialize this as a function returning values from a pareto distribution
        self.competition_history = DataFrame()
        
    def update_competition_history(series):
        self.competition_history.add(agent)