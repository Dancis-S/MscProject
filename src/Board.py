"""This file contain code related to setting up the board"""

import src.Tiles as Tiles


# Theo design parts are in location 18,26,31

# Initialises the board creating the 7 * 7 grid and stores them in array for quick access
class Board:
    def __init__(self, player_num):
        self.player_num = player_num  # Determines which board player gets
        self.board = []
        self.populate_board()
        self.initialise_tiles()
        self.colour_borders(player_num)

    # Function to populate the board with tiles
    def populate_board(self):
        for i in range(49):
            self.board.append(Tiles.NormalTile(i))

    # Function that connects the tiles into graph
    def initialise_tiles(self):
        for i in range(49):
            tile = self.board[i]
            # Check which part of the board we are in and determines offset
            if i % 14 >= 7:  # left most is full hexagon
                offset = 0
            else:  # left most is half hexagon
                offset = -1

            # set up the west connection
            if i % 7 == 0:
                tile.west = None
            else:
                tile.west = self.board[i - 1]

            # set up the east connection
            if i % 7 == 6:
                tile.east = None
            else:
                tile.east = self.board[i + 1]

            # North-west set up
            if i - 7 + offset < 0 or (offset == -1 and i % 7 == 0):
                tile.north_west = None
            else:
                tile.north_west = self.board[i - 7 + offset]

            # North-east set up
            if i - 6 + offset < 0 or (offset == 0 and i % 7 == 6):
                tile.north_east = None
            else:
                tile.north_east = self.board[i - 6 + offset]

            # South West set up
            if i + 7 + offset > 48 or (offset == -1 and i % 7 == 0):
                tile.south_west = None
            else:
                tile.south_west = self.board[i + 7 + offset]

            # South East set up
            if i + 8 + offset > 48 or (offset == 0 and i % 7 == 6):
                tile.south_east = None
            else:
                tile.south_east = self.board[i + 8 + offset]

    # Function that will set the border colours
    def colour_borders(self, player_num):
        pass

    # Given a tile print its info
    def get_tile_info(self, tile_id):
        info = "============================\n Tile ID: " + str(tile_id) + "\n"
        tile = self.board[tile_id]
        if tile.west is None:
            info += "West: None\n"
        else:
            info += "West: " + str(tile.west.tile_id) + "\n"

        if tile.east is None:
            info += "East: None\n"
        else:
            info += "East: " + str(tile.east.tile_id) + "\n"
        if tile.north_west is None:
            info += "North West: None\n"
        else:
            info += "North West: " + str(tile.north_west.tile_id) + "\n"

        if tile.north_east is None:
            info += "North East: None\n"
        else:
            info += "North East: " + str(tile.north_east.tile_id) + "\n"

        if tile.south_west is None:
            info += "South West: None\n"
        else:
            info += "South West: " + str(tile.south_west.tile_id) + "\n"

        if tile.south_east is None:
            info += "South East: None\n"
        else:
            info += "South East: " + str(tile.south_east.tile_id) + "\n"

        info += "============================\n"
        return info

