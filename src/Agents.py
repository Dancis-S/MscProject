""" File that contains the different AI agents"""
import copy
import random
from tensorflow.keras.models import load_model
import numpy as np


class DQNPlayer:
    def __init__(self, agent_id, model_path):
        self.id = agent_id
        self.model = load_model(model_path)

    def get_action(self, game):
        valid_positions = game.get_action_state()
        state = game.getState()

        # State should be preprocessed in the same way as during training
        q_values = self.model.predict(np.array([state]))  # The model expects input in batch form

        # Create array that only gives valid moves
        valid_moves = [True] * 198
        for i in range(1, 199):
            if i not in valid_positions:
                valid_moves[i - 1] = False

        # Convert valid_moves_here to a NumPy array
        valid_moves_array = np.array(valid_moves)

        # Remove all the moves that are not valid
        valid_q_values = q_values.copy()
        valid_q_values[:, ~valid_moves_array] = -np.inf

        best_action = np.argmax(valid_q_values)

        mapped_actions = dqn_convert_move()
        action = mapped_actions[best_action + 1]
        print(action)
        return action





class RandomAgent:
    def __init__(self, player_id):
        self.id = player_id

    def get_action(self, game):
        board = game.get_my_board(self.id)
        open_positions = board.open_positions
        stack = game.get_my_stack(self.id)
        shop = game.shop

        chosen_tile = random.choice(range(len(stack)))
        chosen_location = random.choice(open_positions)
        chosen_shop = random.choice(range(len(shop)))

        # Chosen tile index, chosen position index, tile shop index
        return (chosen_location, chosen_tile, chosen_shop)


class GreedyAgentRandom:
    def __init__(self, player_id):
        self.id = player_id

    def get_action(self, game):
        # Check the open positions
        # Try all possible combinations and return the move that maxes possible increase
        # Otherwise make a random move!
        highest_increase = -1
        best_move = None  # The best possible move, shop is randomised though
        board = game.get_my_board(self.id)
        my_stack = game.get_my_stack(self.id)
        open_positions = board.open_positions

        for position in open_positions:
            # Simulate trying all 3 different tiles in your stack
            for tile in my_stack:
                clone_board = copy.deepcopy(board)
                initial_score = clone_board.get_score()
                clone_board.add_tile(position, tile[0], tile[1])
                change_in_score = clone_board.get_score() - initial_score
                if change_in_score > highest_increase:
                    highest_increase = change_in_score
                    best_move = (position, tile)

        return (best_move[0], my_stack.index(best_move[1]), random.choice(range(3)))

