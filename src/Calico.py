"""This file contain code for playing Calico """
from src import Board


# Will have a main board initialised

# Then initialise the number of players

# Then initialise the game (Giving out the tiles etc.)
class Calico:
    def __init__(self, num_of_players):
        self.shop = []  # Shop that holds available tiles
        self.players_board = []  # Holds the boards for each player
        self.players_stack = []  # Holds the stack for each player
        self.setup_game(num_of_players)

    def setup_game(self, num_of_players):
        """
        Function initialises the array with the players boards, the randomly assigned tiles they have
        in their stack, and initialises the shop
        of players
        :param num_of_players:
        :return:
        """
        # For now makes all the boards purple
        for i in range(num_of_players):
            self.players_board.append(Board.Board(1))  # !!! Change to i later

    def start_game(self, num_of_players):
        """
        Begins the game and loops through all the players giving them a turn to make a play
        :return:
        """
        for i in range(25):
            for n in range(num_of_players):
                print("It's player " + str(n) + "'s move, your stack of tiles is")

                board = self.players_board[n]  # gets the board for the respective players

    def calculate_scores(self):
        """
        Calculates the scores at the end of the game for each player, and determines the winner also
        :return:
        """
        pass
