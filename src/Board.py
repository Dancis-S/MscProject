"""This file contain code related to setting up the board"""

import src.Tiles as Tiles


# Initialises the board creating the 7 * 7 grid and stores them in array for quick access
class Board:
    def __init__(self, player):
        self.player = player  # Determines which board player gets
        self.board = []
        self.populate_board()
        self.initialise_tiles()

    # Function to populate the board with tiles
    def populate_board(self):
        for i in range(49):
            self.board.append(Tiles.NormalTile(i))

    # Function that connects the tiles into graph
    def initialise_tiles(self):
        pass

    # Function that will set the border colours
    def colour_borders(self):
        pass

