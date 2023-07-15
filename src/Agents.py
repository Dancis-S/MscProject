""" File that contains the different AI agents"""
import random
import ast
import PlayerApi


class RandomAgent:
    @classmethod
    def get_action(cls, state):
        game_state = PlayerApi.GameState(state.players_board[0], state.players_board[0].open_positions,
                                         state.players_stack, state.shop)
        open_positions = game_state.getOpenPositions()
        board = game_state.my_board
        stack = game_state.my_stack
        shop = game_state.shop

        chosen_tile = random.choice(range(len(stack)))
        chosen_location = random.choice(open_positions)
        chosen_shop = random.choice(range(len(shop)))

        # Chosen tile index, chosen position index, tile shop index
        return ( chosen_location,chosen_tile, chosen_shop)
