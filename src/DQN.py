import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque


class ReplayMemory:
    def __init__(self, capacity):
        self.memory = deque(maxlen=capacity)

    def add(self, experience):
        self.memory.append(experience)

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)


class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 128)  # First layer has 128 neurons
        self.fc2 = nn.Linear(128, 256)  # Second layer has 256 neurons
        self.fc3 = nn.Linear(256, 128)  # Third layer has 128 neurons
        self.fc4 = nn.Linear(128, action_size)  # Output layer

    def forward(self, state):
        x = torch.relu(self.fc1(state))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        return self.fc4(x)


def soft_update(local_model, target_model, tau=0.001):
    """Soft update model parameters."""
    for target_param, local_param in zip(target_model.parameters(),
                                         local_model.parameters()):
        target_param.data.copy_(tau * local_param.data + (1.0 - tau) * target_param.data)


class DQNAgent:
    def __init__(self, state_size, action_size, env):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.state_size = state_size
        self.action_size = action_size
        self.memory = ReplayMemory(1000000)

        self.env = env

        self.gamma = 0.999
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.999738

        # 0.999925  Decay after 40000
        # 0.9999774540636716 should decay after 100k
        # 200k decay = 0.99988945

        self.q_network = QNetwork(state_size, action_size).to(self.device)
        self.target_network = QNetwork(state_size, action_size).to(self.device)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=0.001)
        self.t_step = 0
        self.target_update_interval = 1500

        self.current_episode = 0

    def step(self, state, action):
        next_state, reward, done = self.env.step(action)
        next_state = np.array(next_state)
        self.memory.add((state, action, reward, next_state, done))
        self.learn()
        return next_state, reward, done

    def act(self, state):
        if self.current_episode < 100:  # Exploration only
            valid_actions = self.env.get_valid_moves()
            action = np.random.choice(valid_actions)
        else:  # Epsilon-greedy strategy

            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)
            state = torch.from_numpy(state).float().to(self.device)
            if np.random.random() > self.epsilon:  # Exploitation
                q_values = self.q_network(state)
                masked_q_values = q_values.clone()
                invalid_actions = torch.tensor(self.env.get_invalid_actions()).float().to(self.device)
                with torch.no_grad():
                    invalid_actions = torch.tensor(invalid_actions, dtype=torch.long).to(self.device)
                masked_q_values[invalid_actions] = -float('inf')
                action = torch.argmax(masked_q_values).item()
            else:  # Exploration
                valid_actions = self.env.get_valid_moves()
                action = np.random.choice(valid_actions)
        return action

    def learn(self):
        if len(self.memory) < 128:
            return

        experiences = self.memory.sample(128)
        states, actions, rewards, next_states, dones = zip(*experiences)

        states = torch.from_numpy(np.vstack(states)).float().to(self.device)
        actions = torch.from_numpy(np.vstack(actions)).long().to(self.device)
        rewards = torch.from_numpy(np.vstack(rewards)).float().to(self.device)
        next_states = torch.from_numpy(np.vstack(next_states)).float().to(self.device)
        dones = torch.from_numpy(np.vstack(dones).astype(np.uint8)).float().to(self.device)

        q_targets_next = self.target_network(next_states).detach().max(1)[0].unsqueeze(1)
        q_targets = rewards + (self.gamma * q_targets_next * (1 - dones))

        q_expected = self.q_network(states).gather(1, actions)

        criterion = nn.SmoothL1Loss()
        loss = criterion(q_expected, q_targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Increment t_step and update target network if necessary
        self.t_step = (self.t_step + 1) % self.target_update_interval
        if self.t_step == 0:
            soft_update(self.q_network, self.target_network)

        return loss.item()

    def save(self, filepath):
        torch.save(self.q_network.state_dict(), filepath)

    def load_weights(self, path):
        self.q_network.load_state_dict(torch.load(path))
        self.q_network.eval()  # Set the network to evaluation mode

    def get_action(self, state, invalid_actions):
        """Return action based on given state as per trained policy."""
        state = torch.from_numpy(state).float().unsqueeze(0).to(self.device)
        with torch.no_grad():
            action_values = self.q_network(state)

        # Mask invalid actions
        masked_action_values = action_values.clone().cpu().data.numpy()
        masked_action_values[0, invalid_actions] = -float('inf')  # Set them to negative infinity
        return np.argmax(masked_action_values)
