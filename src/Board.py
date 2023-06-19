"""This file contain code related to setting up the board"""

import src.Tiles as Tiles


# Initialises the board creating the 7 * 7 grid and stores them in array for quick access
class Board:
    def __init__(self, player_num):
        self.player_num = player_num  # Determines which board player gets
        self.board = []
        self.populate_board()
        self.initialise_tiles()
        self.colour_borders(9)
        self.open_positions = [8, 9, 10, 11, 12, 15, 16, 18, 19, 22, 23, 24, 26, 29, 31, 32,
                               33, 36, 37, 38, 39, 40]
        self.buttons = {"Red": 0, "Yellow": 0, "Purple": 0, "Blue": 0, "Green": 0, "Navy": 0}

    def populate_board(self):
        """
        Adds the tiles (nodes) that will be used to represent the board
        :return:
        """
        for i in range(49):
            self.board.append(Tiles.NormalTile(i))
        # Insert the Design Pattern tiles in 17,25,30 (we start from 0 not 1)
        self.board[17] = Tiles.DesignGoalTile(17, None)
        self.board[25] = Tiles.DesignGoalTile(25, None)
        self.board[30] = Tiles.DesignGoalTile(30, None)

    def initialise_tiles(self):
        """
        Creates the connections (edges) between the tiles (nodes)
        :return:
        """
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

    def colour_borders(self, player_num):
        """
        Depending on the players number (i.e. which board the player gets) the
        boarders are initialised with their respective colour and pattern
        :param player_num:
        :return:
        """
        # To reduce the amount of code required
        # Yellow-0, red-1, purple-2, blue-3, green-4, navy-5
        # stripes-0, leaf-1, dots-2, plants-3, four-4, plants-5
        colours = ["Yellow", "Red", "Purple", "Blue", "Green", "Navy"]
        patterns = ["Stripes", "Leaf", "Dots", "Plants", "Four", "Plants"]
        borders = [0, 1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 43, 44,
                   45, 46, 47, 48, 41, 34, 27, 20, 13]
        # (colour, pattern)
        purple_board = [(0, 4), (1, 2), (2, 4), (0, 1), (3, 0), (1, 4), (4, 2), (3, 4), (5, 0),
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

        for n in range(len(borders)):  # Applies the chosen colours and patterns
            self.board[borders[n]].colour = colours[chosen_board[n][0]]
            self.board[borders[n]].pattern = patterns[chosen_board[n][1]]

    def add_tile(self, tile_id, colour, pattern):
        """
        This function takes as an input the board position, tile colour, tile pattern
        and then places the given tile into
        :return:
        """
        tile = self.board[tile_id]
        tile.colour = colour
        tile.pattern = pattern
        self.open_positions.remove(tile_id)
        self.check_and_add_buttons(tile_id)  # Calls the function to check whether we have gained a button

    def check_and_add_buttons(self, tile_id):
        """
        Each time a new tile is added, search to see if there is a connection of nodes with
        the same colour. (if there is more than 3 then we call method that adds button to the board)
        :param tile_id:
        :return:
        """
        tile = self.board[tile_id]
        count = 1
        colour = tile.colour
        visited_tiles = [tile_id]  # Keeps track of visited nodes
        cache_neighbors = []

        # Loop through all the matching neighbors
        while True:
            neighbors = tile.get_neighbors()
            neighbors = list(filter(lambda item: item is not None, neighbors))  # Remove any None
            # Loop through all neighbors, add where colour matches and tile isn't visited
            for n in neighbors:
                # Checks if it is a Design tile, then we just skip this neighbor
                if isinstance(n, Tiles.DesignGoalTile):
                    continue

                # If it touches an already complete pattern it becomes part of the pattern
                # In-order to be scored, it as to be a separate group!
                if n.colour == colour and n.part_of_button:
                    count = 0
                    tile.part_of_button = True

                # If it is a free matching tile, then add it to cache
                if n.colour == colour and n.tile_id not in visited_tiles and not n.part_of_button:
                    print("Added tile" + str(n.tile_id))
                    cache_neighbors.append(n.tile_id)  # Add id of tile with matching colour

            if not cache_neighbors:  # If there is no more nodes to visit then break
                break

            # Move to the next node, increment count, add its id to visited
            tile = self.board[cache_neighbors.pop()]
            count += 1
            visited_tiles.append(tile.tile_id)

        if count >= 3:  # if there is more than 3 then we group them together.
            self.buttons[colour] += 1  # increment the amount of that colour buttons
            for n in visited_tiles:
                self.board[n].part_of_button = True

    def get_score(self):
        """
        At the end of the game this function is called, it calculates the players score
        based on the design tiles completed, the buttons scored, and the cats scored.
        :return:
        """
        pass

    def get_tile_info(self, tile_id):
        """
        Given a tile id, return the neighbors of the given node.
        Function used for debugging only
        :param tile_id:
        :return:
        """
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
