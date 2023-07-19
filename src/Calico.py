"""This file contain code that will run the actual game"""
import random
<<<<<<< HEAD
from src import Board
from src import Tiles
=======
import Board
import PlayerApi
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264


class Calico:
    def __init__(self, num_of_players, agents):
        self.num_of_players = num_of_players
        self.tiles_bag = []  # Bag that holds the tiles, that players can draw from to play
        self.shop = []  # Shop that holds available tiles
        self.players_board = []  # Holds the boards for each player
        self.players_stack = []  # Holds the stack for each player
        self.setup_game(num_of_players)
        self.final_score = None

    def setup_game(self, num_of_players):
        """
        Function initialises the array with the players boards, the randomly assigned tiles they have
        in their stack, and initialises the shop
        of players
        :param num_of_players:
        :return:
        """
        # There is 3 of each pattern for each colour set put this into the bag
        colours = ["Yellow", "Red", "Purple", "Blue", "Green", "Navy"]
        patterns = ["Stripes", "Leaf", "Dots", "Plants", "Four", "Reeds"]
        for c in colours:
            for p in patterns:
                for i in range(3):
                    # Add tuple (colour, pattern)
                    self.tiles_bag.append((c, p))

        random.shuffle(self.tiles_bag)  # Shuffles the bag containing tiles

        for i in range(3):  # Fill the shop up with 3 tiles
            self.shop.append(self.tiles_bag.pop())

        # Sets up the boards and the players stacks
        for i in range(num_of_players):
            # Initialises each players stack with random tiles from bag
            self.players_stack.append([self.tiles_bag.pop(), self.tiles_bag.pop(), self.tiles_bag.pop()])
            self.players_board.append(Board.Board(i + 1))

    def start_game(self, num_of_players, agents):
        """
        Begins the game and loops through all the players giving them a turn to make a play
        :return:
        """
        # If not agents are provided it will be a human player
        if not agents:
            open_moves = True
            while open_moves:
                for player in range(num_of_players):
                    self.human_players(player)
                    if not self.players_board[player].open_positions:
                        open_moves = False
        else:  # We make our agents play the game
            num_of_players = len(agents)  # to prevent any bugs
            open_moves = True
            while open_moves:
                for player in range(num_of_players):
                    # Code here for the choice the agent makes
                    bot = agents[player]
<<<<<<< HEAD
                    state = self
                    answer = bot.get_action(state)

                    # All agent actions returned as (location, tile_indx, shop_indx)
                    location = answer[0]
                    chosen_tile = answer[1]
                    shop_tile = answer[2]
                    self.make_a_move(bot.id, location, chosen_tile, shop_tile)

                    # Checks whether game is over
                    if not self.players_board[player].open_positions:
                        open_moves = False
        return self.return_score()
=======
                    board = self.players_board[player]
                    open_positions = board.open_positions
                    current_stack = self.players_stack[player]
                    state = self
                    answer = bot.get_action(state)
                    location = answer[0]
                    chosen_tile = answer[1]
                    shop_tile = answer[2]

                    colour = current_stack[chosen_tile][0]
                    pattern = current_stack[chosen_tile][1]
                    board.add_tile(location, colour, pattern)
                    current_stack.pop(chosen_tile)
                    # Now update the shop
                    current_stack.append(self.shop.pop(shop_tile))  # Pop from shop and add to stack
                    self.shop.append(self.tiles_bag.pop())  # Add random tile from bag to shop
                    if not self.players_board[player].open_positions:
                        open_moves = False
        #scores = self.calculate_scores()
        #print(scores)
        return self.return_score()

    def human_players(self, player):
        board = self.players_board[player]  # gets the board for the respective players
        current_stack = self.players_stack[player]
        print("It's player " + str(player) + "'s move, your stack of tiles is")
        print("Open positions: ", board.open_positions)
        print("Your tiles: " + self.return_player_stack_as_string(player))
        chosen_tile, chosen_location = self.get_user_inputs(board)

        colour = current_stack[chosen_tile][0]
        pattern = current_stack[chosen_tile][1]
        board.add_tile(chosen_location, colour, pattern)
        current_stack.pop(chosen_tile)

        # The user now needs to select a new tile from the shop
        print("The shop has: " + self.return_shop_as_string())
        select = int(input("Select a tile from the shop(1-3): "))
        current_stack.append(self.shop.pop(select - 1))  # Pop from shop and add to stack
        self.shop.append(self.tiles_bag.pop())  # Add random tile from bag to shop
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

    def make_a_move(self, player_id, location, chosen_tile, shop_tile):
        """
        Plays the move that for the given player (prevents a lot of manual
        move making for the agents
        :param player_id:
        :param location:
        :param chosen_tile:
        :param shop_tile:
        :return:
        """
        board = self.get_my_board(player_id)  # Get the board
        my_stack = self.get_my_stack(player_id)  # Get the players stack
        tile = my_stack.pop(chosen_tile)  # Pop their chosen tile

        # Tile is (colour, pattern) tuple so tile[0] = colour, and tile[1] = pattern
        board.add_tile(location, tile[0], tile[1])  # Place chosen tile

        my_stack.append(self.shop.pop(shop_tile))  # Pop from shop and add to stack
        self.shop.append(self.tiles_bag.pop())  # Add random tile from bag to shop

    def human_players(self, player):
        board = self.players_board[player]  # gets the board for the respective players
        current_stack = self.players_stack[player]
        print("It's player " + str(player) + "'s move, your stack of tiles is")
        print("Open positions: ", board.open_positions)
        print("Your tiles: " + str(self.players_stack[player]))
        chosen_tile, chosen_location = self.get_user_inputs(board)

        colour = current_stack[chosen_tile][0]
        pattern = current_stack[chosen_tile][1]
        board.add_tile(chosen_location, colour, pattern)
        current_stack.pop(chosen_tile)

        # The user now needs to select a new tile from the shop
        print("The shop has: " + str(self.shop))
        select = int(input("Select a tile from the shop(1-3): "))
        current_stack.append(self.shop.pop(select - 1))  # Pop from shop and add to stack
        self.shop.append(self.tiles_bag.pop())  # Add random tile from bag to shop

    @classmethod
    def get_user_inputs(cls, board):
        """
        Collects the tile and the location that the user wants to play. Then checks that they
        are valid, if invalid they are prompted again, else return the chosen tile and the move
        :return:
        """
        while True:
            chosen_tile = int(input("Enter your chosen tile(1-3):"))
            if chosen_tile > 3 or chosen_tile < 1:
                print("Invalid option you only have 3 card (1-3)")
            else:
                break

        while True:
            chosen_location = int(input("Enter a tile location:"))
            if chosen_location not in board.open_positions:
                print("Invalid move please pick a valid position")
            else:
                break
        return (chosen_tile - 1), chosen_location

    def return_score(self):
        """
        return just the scores nothing else
        :return:
        """
        scores = []
        for board in self.players_board:
            # (name , score)
            scores.append((board.player_num, board.get_score()))  # Add it in
        return scores

    def calculate_scores(self):
        """
        Gets the scores of all the players, determines the winner and returns all the score
        :return:
        """
        scores = []
        for board in self.players_board:
            # (name , score)
            scores.append((board.player_num, board.get_score()))  # Add it in

<<<<<<< HEAD
        scores.sort(key=lambda a: a[1], reverse=True)  # Sort them in order of who wins
=======
        scores.sort(key=lambda a: a[1], reverse = True)  # Sort them in order of who wins
>>>>>>> 9547a0e8ec4ef8f4222379a007778205e058e264

        # Craft the string that will be returned
        position_names = ["\nFourth Place: ", "\nThird Place: ", "\nSecond Place: ", "\nFirst Place: "]
        final_log = "=====!! End Of Game !!====="
        for player in scores:
            final_log += position_names.pop() + "Player " + str(player[0]) + "!  Score: " + str(player[1])

        return final_log

    def get_my_stack(self, player_id):
        """
        Given the players id, return their respective stack!
        :param player_id:
        :return:
        """
        return self.players_stack[player_id]

    def get_my_board(self, player_id):
        """
        Given a players ID return their respective board!
        :param player_id:
        :return:
        """
        return self.players_board[player_id]

    ##################################################################################################
    ##################   Code for DQN Ignore It ######################################################

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
                state.append([self.requirement_to_one_one(tile.requirement), [0, 0, 0, 0, 0, 0]])
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
        og_open = [8, 9, 10, 11, 12, 15, 16, 18, 19, 22, 23, 24, 26, 29, 31, 32,
                   33, 36, 37, 38, 39, 40]
        open_pos = self.open_positions
        moves = []
        counter = 1
        for tile in og_open:
            if tile not in open_pos:
                for i in range(9):
                    counter += 1
            else:
                for i in range(9):
                    moves.append(counter)
                    counter += 1
        return moves
