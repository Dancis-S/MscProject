import Calico  # assuming this is how you access your API
from src.DQN import DQNAgent  # Adjust import as per your directory structure
import matplotlib.pyplot as plt
import torch
import numpy as np


# First, initialize the environment
env = Calico.Calico(1, [])
state_size = len(env.get_state())
action_size = 198

# Initialize the agent
agent = DQNAgent(state_size, action_size, env)

# Define the number of episodes you want to run
num_episodes = 10000

# Variables for logging
rewards_list = []
loss_list = []
mean_q_values_list = []

# Set up the figures
plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

average = 0
average_100 = 0
counter = 0

# Now, you can start interacting with the environment:
print("!!! Starting Training !!!")
for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    episode_loss = []
    episode_q_values = []

    while not done:
        action = agent.act(state)
        next_state, reward, done = agent.step(state, action)

        # Capture the loss for each step
        loss = agent.learn()
        if loss:
            episode_loss.append(loss)

        # Capture Q-values for each step
        q_values = agent.q_network(
            torch.from_numpy(state).float().to(agent.device)).detach().cpu().numpy()
        episode_q_values.append(np.mean(q_values))

        total_reward += reward
        state = next_state

    average = ((average * episode) + total_reward) / (episode + 1)
    average_100 = ((average_100 * counter) + total_reward) / (counter + 1)
    rewards_list.append(average)
    loss_list.append(np.mean(episode_loss))
    mean_q_values_list.append(np.mean(episode_q_values))

    if episode % 100 == 0:
        print(f"Episode {episode} completed with running average: {average}, and a average 100 of: {average_100} ")
        average_100 = 0
        counter = 0
        # Plotting
        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.plot(rewards_list)
        ax1.set_title("Running Average Reward")

        ax2.plot(loss_list)
        ax2.set_title("Mean Loss")

        ax3.plot(mean_q_values_list)
        ax3.set_title("Mean Q-values")

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

    if episode % 20000 == 0:
        agent.save(f'dqn_episode_{episode}.pth')

    counter += 1
    agent.current_episode += 1

plt.ioff()
agent.save('dqn_final.pth')
