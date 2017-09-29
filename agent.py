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

#        self.prob_of_death = prob_of_death
#        self.age = age
#        self.fitness = fitness # initialize this as a function based upon money and some randomness (or parents)
#        self.actions = list()#self.gather, self.hunt)
#        self.actions.extend(actions)
        
    def update_competition_history(series):
        self.competition_history.add(agent)

    # make this a protected function - to be overloaded or modified with delegates
#    def is_dead(self):
#        is_dead = random.random() < self.prob_of_death
#        return is_dead

#    def get_priority(self):
#        
#    # safer option
#    def gather(self,agents):
#    
#    # riskier option
#    def hunt(self,agents):
#    
#    # take from others
#    def fight(self,agents,):
    
    #
#    def step(self,agents):
#        if self.is_dead():
#            return False
#        self.fitness += 0 # make this go up and down based upon age
#        for action in actions:
#            action(agents)