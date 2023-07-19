""" File that contains the different AI agents"""
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


def dqn_convert_move():
    # Convert the output to a playable move
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
    return mapped_actions


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


"""
class GreedyAgentRandom:
    
    Greedy agent that if it cant complete anything it plays a random move
    
    def get_action(self):


    def get_best_complete(self):
        
        From the ranked ways to score, return the method that will return the greates
        :return:
        

    def rank_choices(self, ):
        

        :return:
        


        return choices
"""
