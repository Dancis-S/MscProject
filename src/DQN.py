import random
<<<<<<< HEAD
from src import Calico
=======
import Calico
import PlayerApi
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

<<<<<<< HEAD
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

=======
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
# Example 3D state array shape
state_shape = (58, 2, 6)  # Assuming a 5x5 grid with 2 channels for the Calico game state

# Example action space size
<<<<<<< HEAD
action_space_size = 198  # Assuming there are 4 possible actions in the game
=======
action_space_size = 198 # Assuming there are 4 possible actions in the game
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

hold_actions = [(8, 0, 0), (8, 0, 1), (8, 0, 2), (8, 1, 0), (8, 1, 1), (8, 1, 2), (8, 2, 0),
                (8, 2, 1), (8, 2, 2), (9, 0, 0), (9, 0, 1), (9, 0, 2), (9, 1, 0), (9, 1, 1),
                (9, 1, 2), (9, 2, 0), (9, 2, 1), (9, 2, 2), (10, 0, 0), (10, 0, 1), (10, 0, 2),
                (10, 1, 0), (10, 1, 1), (10, 1, 2), (10, 2, 0), (10, 2, 1), (10, 2, 2), (11, 0, 0),
                (11, 0, 1), (11, 0, 2), (11, 1, 0), (11, 1, 1), (11, 1, 2), (11, 2, 0), (11, 2, 1),
                (11, 2, 2), (12, 0, 0), (12, 0, 1), (12, 0, 2), (12, 1, 0), (12, 1, 1), (12, 1, 2),
                (12, 2, 0), (12, 2, 1), (12, 2, 2), (15, 0, 0), (15, 0, 1), (15, 0, 2), (15, 1, 0),
                (15, 1, 1), (15, 1, 2), (15, 2, 0), (15, 2, 1), (15, 2, 2), (16, 0, 0), (16, 0, 1),
                (16, 0, 2), (16, 1, 0), (16, 1, 1), (16, 1, 2), (16, 2, 0), (16, 2, 1), (16, 2, 2),
                (18, 0, 0), (18, 0, 1), (18, 0, 2), (18, 1, 0), (18, 1, 1), (18, 1, 2), (18, 2, 0),
                (18, 2, 1), (18, 2, 2), (19, 0, 0), (19, 0, 1), (19, 0, 2), (19, 1, 0), (19, 1, 1),
                (19, 1, 2), (19, 2, 0), (19, 2, 1), (19, 2, 2), (22, 0, 0), (22, 0, 1), (22, 0, 2),
                (22, 1, 0), (22, 1, 1), (22, 1, 2), (22, 2, 0), (22, 2, 1), (22, 2, 2), (23, 0, 0),
                (23, 0, 1), (23, 0, 2), (23, 1, 0), (23, 1, 1), (23, 1, 2), (23, 2, 0), (23, 2, 1),
                (23, 2, 2), (24, 0, 0), (24, 0, 1), (24, 0, 2), (24, 1, 0), (24, 1, 1), (24, 1, 2),
                (24, 2, 0), (24, 2, 1), (24, 2, 2), (26, 0, 0), (26, 0, 1), (26, 0, 2), (26, 1, 0),
                (26, 1, 1), (26, 1, 2), (26, 2, 0), (26, 2, 1), (26, 2, 2), (29, 0, 0), (29, 0, 1),
                (29, 0, 2), (29, 1, 0), (29, 1, 1), (29, 1, 2), (29, 2, 0), (29, 2, 1), (29, 2, 2),
                (31, 0, 0), (31, 0, 1), (31, 0, 2), (31, 1, 0), (31, 1, 1), (31, 1, 2), (31, 2, 0),
                (31, 2, 1), (31, 2, 2), (32, 0, 0), (32, 0, 1), (32, 0, 2), (32, 1, 0), (32, 1, 1),
                (32, 1, 2), (32, 2, 0), (32, 2, 1), (32, 2, 2), (33, 0, 0), (33, 0, 1), (33, 0, 2),
                (33, 1, 0), (33, 1, 1), (33, 1, 2), (33, 2, 0), (33, 2, 1), (33, 2, 2), (36, 0, 0),
                (36, 0, 1), (36, 0, 2), (36, 1, 0), (36, 1, 1), (36, 1, 2), (36, 2, 0), (36, 2, 1),
                (36, 2, 2), (37, 0, 0), (37, 0, 1), (37, 0, 2), (37, 1, 0), (37, 1, 1), (37, 1, 2),
                (37, 2, 0), (37, 2, 1), (37, 2, 2), (38, 0, 0), (38, 0, 1), (38, 0, 2), (38, 1, 0),
                (38, 1, 1), (38, 1, 2), (38, 2, 0), (38, 2, 1), (38, 2, 2), (39, 0, 0), (39, 0, 1),
                (39, 0, 2), (39, 1, 0), (39, 1, 1), (39, 1, 2), (39, 2, 0), (39, 2, 1), (39, 2, 2),
                (40, 0, 0), (40, 0, 1), (40, 0, 2), (40, 1, 0), (40, 1, 1), (40, 1, 2), (40, 2, 0),
                (40, 2, 1), (40, 2, 2)]

mapped_actions = {}
num = 1
for n in hold_actions:
    mapped_actions[num] = n
    num += 1

<<<<<<< HEAD

# Create the DQN model
def create_dqn_model():
    model = models.Sequential()

    # Convolutional Layers
    model.add(layers.Conv2D(32, (2, 1), activation='relu', padding='same', input_shape=state_shape))
    model.add(layers.MaxPooling2D((2, 1)))

    model.add(layers.Conv2D(64, (2, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 1)))

    model.add(layers.Conv2D(128, (2, 1), activation='relu', padding='same'))
    model.add(layers.MaxPooling2D((2, 1)))

    model.add(layers.Flatten())

    # Dense Layers
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(action_space_size))  # Output layer with size equal to action space

=======
# Create the DQN model
def create_dqn_model():
    model = models.Sequential()
    model.add(layers.Conv2D(32, (2, 2), activation='relu', input_shape=state_shape))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(action_space_size))  # Output layer with size equal to action space
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
    return model


# Instantiate the DQN model
dqn_model = create_dqn_model()
<<<<<<< HEAD
dqn_model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=0.001))
=======
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

# Define the loss function and optimizer
loss_function = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)


# Function to preprocess the state and action for DQN input
def preprocess_state(state):
    # Perform any necessary preprocessing on the state array
    # (e.g., normalization, reshaping, scaling, etc.)
    return state


def preprocess_action(action):
    # Perform any necessary preprocessing on the action vector
    # (e.g., one-hot encoding, scaling, etc.)
    return action


# Function to select an action based on the current state using the DQN
def select_action(state, valid_positions):
    preprocessed_state = preprocess_state(state)
    q_values = dqn_model.predict(np.expand_dims(preprocessed_state, axis=0))

    # Create array that only gives valid moves
    valid_moves = [True] * 198
    for i in range(1, 199):
        if i not in valid_positions:
<<<<<<< HEAD
            valid_moves[i - 1] = False
=======
            valid_moves[i-1] = False
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

    # Convert valid_moves_here to a NumPy array
    valid_moves_array = np.array(valid_moves)

    # Filter out invalid actions by setting their Q-values to -inf
    valid_q_values = q_values.copy()
    valid_q_values[:, ~valid_moves_array] = -np.inf

    best_action = np.argmax(valid_q_values)
    return best_action + 1


# Function to store experiences in the replay buffer
def store_experience(state, action, reward, next_state, done):
    preprocessed_state = preprocess_state(state)
    preprocessed_next_state = preprocess_state(next_state)
    preprocessed_action = preprocess_action(action)
<<<<<<< HEAD
    if len(replay_buffer) > 1400:
        replay_buffer.pop(0)
=======
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
    replay_buffer.append((preprocessed_state, preprocessed_action, reward, preprocessed_next_state, done))


# Function to train the DQN using a mini-batch of experiences from the replay buffer
def train_dqn():
    batch_size = 32
    if len(replay_buffer) < batch_size:
        return

    # Sample a mini-batch of experiences from the replay buffer
    minibatch = random.sample(replay_buffer, batch_size)

    states, actions, rewards, next_states, dones = zip(*minibatch)
    states = np.array(states)
    actions = np.array(actions)
    rewards = np.array(rewards)
    next_states = np.array(next_states)
    dones = np.array(dones)

    # Preprocess the states and actions
    preprocessed_states = preprocess_state(states)
    preprocessed_next_states = preprocess_state(next_states)
    preprocessed_actions = preprocess_action(actions)

    # Compute the target Q-values using the Bellman equation
    target_q_values = rewards + (1 - dones) * np.amax(dqn_model.predict(preprocessed_next_states), axis=1)

    # Reshape the target Q-values to match the predicted Q-values
    target_q_values = np.reshape(target_q_values, (-1, 1))

    # Update the Q-values for the selected actions
    with tf.GradientTape() as tape:
        predicted_q_values = dqn_model(preprocessed_states)
        loss = loss_function(target_q_values, predicted_q_values)

    gradients = tape.gradient(loss, dqn_model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, dqn_model.trainable_variables))

<<<<<<< HEAD

=======
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
def take_action(game, action):
    """
    First we translate the action back to the mapping, then we carry out the play,
    and then return the new state of the board, along with the reward, and whether
    the game is finished or not
    :return:
    """
    # Convert here
    tup = mapped_actions[action]
    location = tup[0]
    stack_indx = tup[1]
    shop_indx = tup[2]

    # Then with the given tuple just add the tile where need be
    board = game.players_board[0]
    stack = game.players_stack[0]
    shop = game.shop
    colour = stack[stack_indx][0]
    pattern = stack[stack_indx][1]
    board.add_tile(location, colour, pattern)

    # Add the selected shop item to the players stack, and then add random item to shop from bag
    stack.pop(stack_indx)  # Pop the used tile
    stack.append(shop.pop(shop_indx))  # Add the selected tile
    shop.append(game.tiles_bag.pop())  # Pull rand out of bag to fill shop again

    # What gets returned!
    if not board.open_positions:
        comp_reward = board.get_score()
        comp_done = True
    else:
        comp_reward = -0.5
        comp_done = False

<<<<<<< HEAD
    new_state = game.getState()

    return new_state, comp_reward, comp_done

=======
    newApi = PlayerApi.GameState(board, board.open_positions, stack, shop)
    newState = newApi.getState()

    return newState, comp_reward, comp_done
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

def initialize_state(game):
    """
    Return the initial state of the game
    :param game:
    :return:
    """
<<<<<<< HEAD
    return game.getState()  # Returns the array holding the state of the game


# Training loop
num_episodes = 10000  # Number of episodes for training
=======
    board = game.players_board[0]
    open_pos = board.open_positions
    stack = game.players_stack[0]
    shop = game.shop
    api = PlayerApi.GameState(board, open_pos, stack, shop)
    return api.getState()  # Returns the array holding the state of the game


# Training loop
num_episodes = 10  # Number of episodes for training
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
replay_buffer = []  # Replay buffer to store experiences

for episode in range(num_episodes):
    game = Calico.Calico(1, [])
    state = initialize_state(game)  # Your function to initialize the game state
<<<<<<< HEAD
=======
    api = PlayerApi.GameState(game.players_board[0], game.players_board[0].open_positions, game.players_stack[0], game.shop)
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
    done = False
    print("Episode = " + str(episode))

    while not done:
<<<<<<< HEAD
        action = select_action(state, game.get_action_state())
        next_state, reward, done = take_action(game,
                                               action)  # Your function to advance the game state based on the action
=======
        action = select_action(state, api.get_action_state())
        next_state, reward, done = take_action(game, action)  # Your function to advance the game state based on the action
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264
        store_experience(state, action, reward, next_state, done)
        train_dqn()
        state = next_state

# Save the trained model
dqn_model.save("agh.keras")
# Use the trained DQN to play the game or make predictions
