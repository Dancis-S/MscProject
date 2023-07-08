"""This file contain code that will run the actual game"""
import random
from src import Board
from src import PlayerApi


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
        patterns = ["Stripes", "Leaf", "Dots", "Plants", "Four", "Plants"]
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
                    board = self.players_board[player]
                    open_positions = board.open_positions
                    current_stack = self.players_stack[player]
                    state = PlayerApi.GameState(board, open_positions, current_stack, self.shop)

                    chosen_tile, chosen_location, shop_tile = bot.getAction(state)  # Returns indexes

                    colour = current_stack[chosen_tile][0]
                    pattern = current_stack[chosen_tile][1]
                    location = open_positions[chosen_location]
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

    def get_user_inputs(self, board):
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

        scores.sort(key=lambda a: a[1], reverse = True)  # Sort them in order of who wins

        # Craft the string that will be returned
        position_names = ["\nFourth Place: ", "\nThird Place: ", "\nSecond Place: ", "\nFirst Place: "]
        final_log = "=====!! End Of Game !!====="
        for player in scores:
            final_log += position_names.pop() + "Player " + str(player[0]) + "!  Score: " + str(player[1])

        return final_log

    def return_shop_as_string(self):
        """
        Function that will print the current tile in the shop that are available for players to take
        :return:
        """
        return str(self.shop)

    def return_player_stack_as_string(self, current_player):
        """
        Prints the tiles that are in the players stack and available for play
        :return:
        """
        return str(self.players_stack[current_player])

