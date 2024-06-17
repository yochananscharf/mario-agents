'''
Mario vs. Bowser
Final project in the course: Multiagent Systems and Distributed Systems

 

Agent class. Represents an agent in a game. Can be trained for optimal strategies using
the Shapely value iteration algorithm. 
'''
 

import random
from game import *

class agent:
    # Initializer
    def __init__(self,game,player):
        self.game = game
        self.player = player
        self.optimal_strategies = {}
        pass

    # General train method. More functionality can be added to allow for more than
    # one training method, but for now it simply calls the Shapely method.
    def train(self):
        self.optimal_strategies = self.train_value_iteration()
        return 
        # if self.player == 1:
        #     self.optimal_strategies = {(1,3):'up',(4,6):'right',(1,6):'up',(4,2):'right', (2,6):'up', (2,3):'up', (2,6):'up', (4,3):'right'}
        # if self.player == 2:
        #     self.optimal_strategies = {(1,3):'up',(4,6):'left',(1,6):'left',(4,2):'up', (2,6):'left', (2,3):'up', (2,6):'up', (4,3):'up'}
        # return 
        
    
    def print_optimal_strategies(self):
        print(self.optimal_strategies)
        pass
 
    def get_random_strategy(self, state):
        actions = self.game.states[state-1].actions
        random_action = random.choice(actions)
        return random_action
    

    def train_value_iteration(self):

        states = [(1,3),(1,2), (4,6),(1,6),(4,2), (2,6), (2,3), (4,3), (5,2), (5,6), (2, 5), (5,5), (4,5), (2,2)]
        policy, v = self.value_iteration(states, 0.9, 0.001 )
        return policy

    #def value_iteration(states, actions, transition_model, reward_function, gamma, epsilon):
    def value_iteration(self, states, gamma, epsilon):
        # Initialize value function
        
        V = {s: 0 for s in states}
        if self.player == 1:
            agnt = 0
            oppnt = 1
        else:
            agnt = 1
            oppnt = 0
        while True:
            delta = 0
            for state in states:
                
                state_agent = state[agnt]
                state_opponent = state[oppnt]
                if (state_agent == 5) or (state_opponent == 5) or (state_agent == state_opponent):
                    continue
                actions = self.game.states[state_agent-1].actions
                actions_opponent = self.game.states[state_opponent-1].actions
                
                action_pairs = [(action_a, action_o) for action_a in actions for action_o in actions_opponent]
                transitionVals = [self.game.P(state_agent, self.game.states[state_agent-1].outcomes[actn_agnt], actn_agnt, state_opponent,  actn_opnt) for (actn_agnt,actn_opnt ) in action_pairs]
                rewardVals = [self.game.R(state_agent, self.game.states[state_agent-1].outcomes[actn_agnt], actn_agnt, state_opponent,  actn_opnt) for (actn_agnt,actn_opnt ) in action_pairs]
                ds_opponent = [self.game.states[state_opponent-1].outcomes[actn_opnt] for _, actn_opnt in action_pairs]
                ds_agent = [self.game.states[state_agent-1].outcomes[actn_agnt] for actn_agnt, _ in action_pairs]

                v = V[state]

                if self.player == 1:
                    dest_pairs = list(zip(ds_agent,ds_opponent))
                    discounted = [gamma * V[(dest_a,dest_o )] for (dest_a, dest_o) in dest_pairs]
                else:
                    dest_pairs = list(zip(ds_opponent, ds_agent))
                    discounted = [gamma * V[(dest_o, dest_a)] for (dest_o, dest_a) in dest_pairs]
                sum_discounted = [rewardVals[i] * transitionVals[i] + discounted[i] for i in range(len(actions))]
                V[state] = max(sum_discounted)

                delta = max(delta, abs(v - V[state]))
            
            # Check for convergence
            if delta < epsilon:
                break
    
        # Extract optimal policy
        policy = {}
        for state in states:
            state_agent = state[agnt]
            state_opponent = state[oppnt]
            if (state_agent == 5) or (state_opponent == 5)or (state_agent == state_opponent):
                continue
            actions = self.game.states[state_agent-1].actions
            actions_opponent = self.game.states[state_opponent-1].actions

            action_pairs = [(action_a, action_o) for action_a in actions for action_o in actions_opponent]
            transitionVals = [self.game.P(state_agent, self.game.states[state_agent-1].outcomes[actn_agnt], actn_agnt, state_opponent,  actn_opnt) for (actn_agnt,actn_opnt ) in action_pairs]
            rewardVals = [self.game.R(state_agent, self.game.states[state_agent-1].outcomes[actn_agnt], actn_agnt, state_opponent,  actn_opnt) for (actn_agnt,actn_opnt ) in action_pairs]
            ds_opponent = [self.game.states[state_opponent-1].outcomes[actn_opnt] for _, actn_opnt in action_pairs]
            ds_agent = [self.game.states[state_agent-1].outcomes[actn_agnt] for actn_agnt, _ in action_pairs]

            if self.player == 1:
                dest_pairs = list(zip(ds_agent,ds_opponent))
                discounted = [gamma * V[(dest_a,dest_o )] for (dest_a, dest_o) in dest_pairs]
            else:
                dest_pairs = list(zip(ds_opponent, ds_agent))
                discounted = [gamma * V[(dest_o, dest_a)] for (dest_o, dest_a) in dest_pairs]
            
            sum_discounted = [rewardVals[i] * transitionVals[i] + discounted[i] for i in range(len(dest_pairs))]
            policy[state] = max(actions, key =lambda a: sum_discounted)

        return policy, V
