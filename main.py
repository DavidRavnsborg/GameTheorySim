# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:55:05 2017

Game Theory Simulation
Based on: http://ncase.me/trust/

@author: David
"""

from agent import Agent
from pandas import DataFrame
import strategies as st

NUM_OF_COPYCATS = 5
NUM_OF_COOPERATORS = 5
NUM_OF_CHEATERS = 5
NUM_OF_GRUDGERS = 5
NUM_OF_DETECTIVES = 5
    
def prisoners_dilemma(agents, num_of_rounds):
    both_cooperate = (2,2)
    both_cheat = (0,0)
    one_cheat = (3,-1)

    for agent1 in agents:
        for agent2 in agents:
            if agent2.name == agent1.name:
                continue

            print("Prisoner's dilemma: {} {}".format(agent1.name, agent2.name))
            agent1_actions = list()
            agent2_actions = list()
            for i in range(num_of_rounds):
                result1 = agent1.strategy(agent2_actions)
                result2 = agent2.strategy(agent1_actions)
                agent1_actions.append(result1)
                agent2_actions.append(result2)
                if result1 == 1 and result2 == 1:
                    agent1.score_history.append(agent1.score_history[-1]+both_cooperate[0])
                    agent2.score_history.append(agent2.score_history[-1]+both_cooperate[1])
                elif result1 == 1 and result2 == -1:
                    agent1.score_history.append(agent1.score_history[-1]+one_cheat[1])
                    agent2.score_history.append(agent2.score_history[-1]+one_cheat[0])
                elif result1 == -1 and result2 == 1:
                    agent1.score_history.append(agent1.score_history[-1]+one_cheat[0])
                    agent2.score_history.append(agent2.score_history[-1]+one_cheat[1])
                elif result1 == -1 and result2 == -1:
                    agent1.score_history.append(agent1.score_history[-1]+both_cheat[0])
                    agent1.score_history.append(agent2.score_history[-1]+both_cheat[1])
                else:
                    print('Invalid results, Agent1 result: {}; Agent2 result: {}'
                          .format(result1,result2))
            
agents = list()
for i in range(NUM_OF_COPYCATS):
    agents.append(Agent('Copycat', i, st.copycat_strategy))
for i in range(NUM_OF_COOPERATORS):
    agents.append(Agent('Cooperator', i, st.cooperator_strategy))
for i in range(NUM_OF_CHEATERS):
    agents.append(Agent('Cheater', i, st.cheater_strategy))
for i in range(NUM_OF_GRUDGERS):
    agents.append(Agent('Grudger', i, st.grudger_strategy))
for i in range(NUM_OF_DETECTIVES):
    agents.append(Agent('Detective', i, st.detective_strategy))
        
prisoners_dilemma(agents,5)

results_dict = {}
for agent in agents:
    results_dict[agent.name] = agent.score_history
print(results_dict)
results_df = DataFrame(results_dict)
print(results_df.iloc[-1,:])