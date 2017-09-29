# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:43:34 2017

@author: David
"""

def copycat_strategy(previous_actions):
    if len(previous_actions) == 0:
        return 1
    else:
        return previous_actions[-1]

def cooperator_strategy(previous_actions):
    return 1

def cheater_strategy(previous_actions):
    return -1

def grudger_strategy(previous_actions):
    if -1 in previous_actions:
        return -1
    else:
        return 1

def detective_strategy(previous_actions):
    num_of_previous_rounds = len(previous_actions)
    if num_of_previous_rounds == 0:
        return 1
    elif num_of_previous_rounds == 1:
        return -1
    elif num_of_previous_rounds == 2:
        return 1
    elif num_of_previous_rounds == 3:
        return 1
    else:
        if -1 in previous_actions:
            return previous_actions[-1]
        else:
            return -1    