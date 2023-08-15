""" File that contains the different AI agents"""
import copy
import random
import src.DQN as DQN
import os


class RandomAgent:
    """
    Class that contain code for the random agent
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.player_name = "Random Agent"
    def get_action(self, game):
        """
        Given a game state, returns a random move to play
        """
        board = game.get_my_board(self.player_id)
        open_positions = board.open_positions
        stack = game.get_my_stack(self.player_id)
        shop = game.shop

        chosen_tile = random.choice(range(len(stack)))
        chosen_location = random.choice(open_positions)
        chosen_shop = random.choice(range(len(shop)))

        # Chosen tile index, chosen position index, tile shop index
        return chosen_location, chosen_tile, chosen_shop

    def my_id(self):
        """
        Prints the agents id
        """
        print(self.player_id)


class DQNAgent:
    def __init__(self, device='cpu'):
        self.dqn = DQN.DQNAgent(678, 198, device)
        self.model_path = self.set_path()
        self.dqn.load_weights(self.model_path)
        self.player_id = 0
        self.player_name = "DQN Agent"

    def get_action(self, game):
        """Receive the current game state and decide on the next action."""
        game_state = game.get_state()
        invalid_actions = game.get_invalid_actions()
        action = self.dqn.get_action(game_state, invalid_actions)
        mapped_moves = game.dqn_convert_move()
        play = mapped_moves[action]
        return play

    def set_path(self):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Assuming your CSV files are in the same directory as your script
        file_path = os.path.join(script_dir, 'dqn_final.pth')
        return file_path


class GreedyAgentRandom:
    """
    Class for the greedy agent
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.player_name = "Greedy Agent_" + str(self.player_id)

    def get_action(self, game):
        """
        Given a game state returns the best move, using the greedy approach
        """
        # Check the open positions
        # Try all possible combinations and return the move that maxes possible increase
        # Otherwise make a random move!
        highest_increase = -1
        best_move = None  # The best possible move, shop is randomised though
        board = game.get_my_board(self.player_id)
        my_stack = game.get_my_stack(self.player_id)
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

        return best_move[0], my_stack.index(best_move[1]), random.choice(range(3))

    def my_id(self):
        """
        Prints the agents id
        """
        print(self.player_id)
