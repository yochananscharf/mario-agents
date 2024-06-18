# Multi Agent Mini-Project

Given an enviroment and two agents (Mario and Bowser).

The goal is to write an algorithm that trains the two agents to navigate the environment while maximising thier reward.


## Value iteration MDP
We implemented a value-iteration process.

The value-iteration process is an MDP (Markov Decision Process) which solves Belmman's equation.


![bellman](https://github.com/yochananscharf/mario-agents/assets/10595146/ee1ca209-788b-4bf7-a250-a3aad4a9090c)

 
 
## Markov Decision Processes
 
 - **States (S):** A finite set of states that represent all - possible situations in the environment.
- **Actions (A):** A finite set of actions available to the agent.
- **Transition Model (P):** The probability P(s′∣s, a)P(s′∣s, a) of transitioning from state ss to state s′s′ after taking action aa.
- **Reward Function (R):** The immediate reward received after transitioning from state ss to state s′s′ due to action aa.
- **Discount Factor (γ):** A factor between 0 and 1 that represents the present value of future rewards.
 
 
 
 ## Key Steps of the Value Iteration Algorithm
 
 
 1. Initialization: we start from initializing the utility of every state as zero and we set γ as 0.5. We then loop through states using the Bellman equation.

 2. Value Update: Iteratively update the value function using the Bellman equation: `Vk+1(s)=max⁡a∈A∑s′P(s′∣s, a)[R(s, a,s′)+γVk(s′)]Vk+1​(s)=a∈Amax​s′∑​P(s′∣s, a)[R(s, a,s′)+γVk​(s′)]` This equation calculates the expected cumulative reward for taking action `a` in state `s` and then following the optimal policy thereafter.
 3. Convergence Check: Continue the iteration until the value function converges, i.e., the change in the value function between iterations is smaller than a predefined threshold ϵ.
 4. Extract Policy: Once the value function has converged, the optimal policy can be derived by selecting the action that maximizes the expected cumulative reward:π∗(s)=arg⁡max⁡a∈A∑s′P(s′∣s, a)
 
 `[R(s, a,s′)+γV∗(s′)]π∗(s)=arga∈Amax​s′∑​P(s′∣s, a)[R(s, a,s′)+γV∗(s′)]`
 
 ## Results
 
 Running the algorith yields an optimal policy for each agent respectively.
 
**Optimal-policy-Mario:**
`{(1, 3): 'right', (1, 2): 'right', (4, 6): 'right', (1, 6): 'right', (4, 2): 'right', (2, 6): 'up', (2, 3): 'up', (4, 3): 'right'}`

**Optimal-policy-Bowser:**
`{(1, 3): 'left', (1, 2): 'up', (4, 6): 'left', (1, 6): 'left', (4, 2): 'up', (2, 6): 'left', (2, 3): 'left', (4, 3): 'left'}`
 
 ### Sources
 
https://www.geeksforgeeks.org/implement-value-iteration-in-python/

https://medium.com/@ngao7/markov-decision-process-value-iteration-2d161d50a6ff

