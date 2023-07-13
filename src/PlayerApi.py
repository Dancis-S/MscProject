""" api that will be used by the AI agents to get info about the game and interact
    with the game"""
import numpy

from src import Tiles


class GameState:
    def __init__(self, board, open_positions, stack, shop):
        """
        This is holds all the information that the agent might need to access,
        """
        self.my_board = board
        self.open_positions = open_positions
        self.shop = shop
        self.my_stack = stack

    def getOpenPositions(self):
        return self.open_positions

    def colour_info_to_one_hot(self, colour):
        """
       Converts the string of colour into a one-hot encoded version
       :param colour:
       :return:
       """
        word_colours = ["Yellow", "Red", "Purple", "Blue", "Green", "Navy"]
        encoded_colour = []
        for word in word_colours:
            if word == colour:
                encoded_colour.append(1)
            else:
                encoded_colour.append(0)

        return encoded_colour

    def patter_info_to_one_hot(self, pattern):
        """
        Converts the string of pattern into a one-hot encoded version
        :param pattern:
        :return:
        """
        # [Stripes, Leaf, Dots, Plants, Four, Reeds]
        encoded_pattern = []
        word_patterns = ["Stripes", "Leaf", "Dots", "Plants", "Four", "Reeds"]
        for word in word_patterns:
            if word == pattern:
                encoded_pattern.append(1)
            else:
                encoded_pattern.append(0)

        return encoded_pattern

    def requirement_to_one_one(self, requirement):
        """
        Converts the string requirements into a one-hot encoded version
        :param requirement:
        :return:
        """
        encoded_requirements = []
        word_req = ["NotEqual", "aaa-bbb", "aa-bb-cc", "aaaa-bb", "aaa-bb-c", "aa-bb-c-d"]
        for req in word_req:
            if requirement == req:
                encoded_requirements.append(1)
            else:
                encoded_requirements.append(0)
        return encoded_requirements

    def getState(self):
        state = []  # Array that will hold the 3D state of the game

        # Add the cats to the game state
        cats = self.my_board.cats
        for cat in cats:
            cat_info = [self.patter_info_to_one_hot(cat.pattern_1), self.patter_info_to_one_hot(cat.pattern_2)]
            state.append(cat_info)

        # Add the board positions 0 means open position
        for tile in self.my_board.board:
            if isinstance(tile, Tiles.DesignGoalTile):
                # In situation where it's a design tile we need to add its requirements
                state.append([self.requirement_to_one_one(tile.requirement),[0, 0, 0, 0, 0, 0]])
            elif tile.colour is None or tile.pattern is None:
                state.append([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])  # Free tile
            else:
                info = [self.colour_info_to_one_hot(tile.colour), self.patter_info_to_one_hot(tile.pattern)]
                state.append(info)

        # Add the player stack
        for tile in self.my_stack:
            info = [self.colour_info_to_one_hot(tile[0]), self.patter_info_to_one_hot(tile[1])]
            state.append(info)

        # Add the shop stack
        for tile in self.shop:
            info = [self.colour_info_to_one_hot(tile[0]), self.patter_info_to_one_hot(tile[1])]
            state.append(info)

        return state

    def get_action_state(self):
        """
        og_open_positions = [8, 9, 10, 11, 12, 15, 16, 18, 19, 22, 23, 24, 26, 29, 31, 32,
                             33, 36, 37, 38, 39, 40]
        mover = 1
        actions = []
        for pos in og_open_positions:
            if pos in self.open_positions:
                for i in range(9):
                    actions.append(mover)
                    mover += 1
            else:
                for i in range(9):
                    mover += 1

        """
        moves = []
        for tile_board in self.open_positions:
            for tile_stack in range(3):
                for tile_shop in range(3):
                    moves.append((tile_board, tile_stack, tile_shop))

        return moves


    def getBoard(self):
        """ We might change this later!"""
        return self.my_board

    def getStack(self):
        return self.my_stack

    def getShop(self):
        return self.shop
