"""This file contain code related to setting up the board"""

import Tiles


# Initialises the board creating the 7 * 7 grid and stores them in array for quick access
class Board:
    def __init__(self, mode):
        self.mode = mode
        self.board = []
        self.initialise_tiles()

    # Function that creates all the nodes (tiles) in the board
    def initialise_tiles(self):
        nahala = self.board
        for i in range(49):
            self.board.append(Tiles.NormalTile(i))
            
    def test_board(self):
        mhm = self.mode
        stuff = self.board
        for n in stuff:
            print(n.get_id())


test = Board("easy")
test.test_board()
