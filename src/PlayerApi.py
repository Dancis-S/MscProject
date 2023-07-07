""" api that will be used by the AI agents to get info about the game and interact
    with the game"""


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

    def getBoard(self):
        """ We might change this later!"""
        return self.my_board

    def getStack(self):
        return self.my_stack

    def getShop(self):
        return self.shop
