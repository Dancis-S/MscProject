import torch
import Calico  # assuming this is how you access your API
from src.DQN import DQNAgent  # Adjust import as per your directory structure

# First, initialize the environment
env = Calico.Calico(1, [])

# Assume that 'get_state' method gives you the current state as a flattened list
state_size = len(env.get_state())
action_size = 198  # I'm assuming there's a function to get the size of the action space

# Initialize the agent
agent = DQNAgent(state_size, action_size, env)

# Define the number of episodes you want to run
num_episodes = 200000

average = 0
average_100 = 0
counter = 0
# Now, you can start interacting with the environment:
print("!!! Starting Training !!!")
for episode in range(num_episodes):
    # Reset the environment and get the initial state
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        # Let the agent select an action
        action = agent.act(state)

        # Perform the action in the environment and get the results
        next_state, reward, done = agent.step(state, action)

        # Update total reward
        total_reward += reward

        # Move to the next state
        state = next_state
    average = ((average * episode) + total_reward) / (episode + 1)
    average_100 = ((average_100 * counter) + total_reward) / (counter + 1)
    if episode % 100 == 0:
        print(f"Episode {episode} completed with running average: {average}, and a 100 average of: {average_100}")
        counter = 0
        average_100 = 0
    if episode % 50000 == 0:  # save the model every 1000 episodes
        agent.save(f'dqn_episode_{episode}.pth')
    counter += 1
    agent.current_episode += 1

def calculate_running_average(previous_avg, new_num, n):
    return ((previous_avg * (n - 1)) + new_num) / n

# save the final model
agent.save('dqn_final.pth')