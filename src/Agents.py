""" File that contains the different AI agents"""
import random


class RandomAgent:
    def getAction(self, GameState):
        open_positions = GameState.getOpenPositions()
        board = GameState.my_board
        stack = GameState.my_stack
        shop = GameState.shop

        chosen_tile = random.choice(range(len(stack)))
        chosen_location = random.choice(range(len(open_positions)))
        chosen_shop = random.choice(range(len(shop)))

        # Chosen tile index, chosen position index, tile shop index
        return chosen_tile, chosen_location, chosen_shop

    def final(self):
        """
        No clue wtf goes on here
        :return:
        """
        print("Hello!")


