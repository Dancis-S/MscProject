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
        # Insert the Design Pattern tiles in 17,25,30 (we start from 0 not 1)
        self.board[17] = Tiles.DesignGoalTile(17, None)
        self.board[25] = Tiles.DesignGoalTile(25, None)
        self.board[30] = Tiles.DesignGoalTile(30, None)

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

    # Function that will set the border colours depending on the player
    def colour_borders(self, player_num):
        # To reduce the amount of code required
        # Yellow-0, red-1, purple-2, blue-3, green-4, navy-5
        # stripes-0, leaf-1, dots-2, plants-3, four-4, plants-5
        colours = ["Yellow", "Red", "Purple", "Blue", "Green", "Navy"]
        patterns = ["Stripes", "Leaf", "Dots", "Plants", "Four", "Plants"]
        borders = [0, 1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 43, 44,
                   45, 46, 47, 48, 41, 34, 27, 20, 13]
        purple_board = [(0, 4), (1, 2), (2, 4), (0, 1), (3, 0), (1, 4), (4, 2), (3, 4), (5,0),
                        (4, 1), (1, 3), (3, 2), (2, 1), (0, 4), (2, 0), (5, 1), (4, 4), (0, 3),
                        (2, 2), (5, 4), (4, 0), (1, 1), (3, 4), (5, 5)]
        blue_board = [()]
        green_board = [()]
        yellow_board = [()]
        chosen_board = None

        if player_num == 1:
            chosen_board = purple_board
        elif player_num == 2:
            chosen_board = blue_board
        elif player_num == 3:
            chosen_board = green_board
        elif player_num == 4:
            chosen_board = yellow_board
        else:  # Default to purple board
            chosen_board = purple_board

        for n in borders:  # Applies the chosen colours and patterns
            self.board[n].colour = colours[chosen_board[n][0]]
            self.board[n].pattern = patterns[chosen_board[n][1]]

    # Given a tile return its info (useful for debugging)
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
