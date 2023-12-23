# AI Investigation in Non-Deterministic Board Games: Calico

## Introduction
Briefly introduce the project and its significance in AI research, particularly in the context of board games.

## About the Game - Calico
Explain the basics of the Calico game, emphasizing elements that are relevant to the AI strategies you explored.

## Objective
Detail the specific goals of your project, including what aspects of AI in non-deterministic, perfect information games you focused on.

## AI Agents Overview
- **Random Agent**: Agent that will play moves at random
- **Greedy Agent**: Agent that will follow the greedy stratergy of maximising immediate reward
- **Monte Carlo Tree Search (MCTS)**: Agent that will follow the MCTS process in determining next move
- **Deep Q-Network (DQN)**: Agent that will use a Deep Q-Network to determine the next best move

## Technologies Used
- Python
- Libraries: NumPy, PyTorch

## Results and Discussion
With the analysis of the results from the head-to-head games and the t-test, we
can confidently rank the agents based on their performance.
1. MCTS Agent
2. Greedy Agent
3. Random Agent and DQN Agent

![Score Distributions](images/all_agents_distribution.png "Distribution of all Agent scores")

The MCTS Agent clearly stands out in its ability to handle the complex environment
of Calico through game simulation. This performance highlights the power of
foresight. Following the MCTS Agent is the Greedy Agent, while not as robust as
the MCTS Agent, still illustrates that maximising for immediate reward can result
in reasonably good outcomes. The DQN Agent, unfortunately, played equivalent
to that of the Random Agent. However, the Random Agent shows that by random
play, one can still score points and, on rare occasions, win games.

The two potential areas that were investigated were: board colour and player turn order. The ANOVA results
suggested that neither board colour provided a significant advantage in the score.
Similarly, the t-test analysis for the first mover advantage between the two greedy
agents showed no statistically significant difference in their scores based on turn
order. Therefore, based on this analysis, Calico seems to be balanced in terms of
the boards and the order of turns. Future work might look further into specific
mechanics to find any potential advantages.

## Class Diagram

![Class Diagram](images/class_diagram.png "Class Diagram for Calico")

