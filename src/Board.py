"""This file contain code related to setting up the board"""

import Tiles


# Initialises the board creating the 7 * 7 grid and stores them in array for quick access
class Board:
    def __int__(self, mode):
        self.board = []
        self.initialise_tiles()

# Function that creates all the nodes (tiles) in the board
    def initialise_tiles(self):
        for i in range(49):
            self.board[i] = Tiles.NormalTile()
