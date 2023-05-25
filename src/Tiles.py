"""Classes that define the tiles that will be used in the game"""


# Class to define the tile object that will be used to represent the nodes in the board
class NormalTile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.pattern = None
        self.colour = "Green"

        # directions
        self.west = None
        self.east = None
        self.north_west = None
        self.north_east = None
        self.south_east = None
        self.south_west = None

    # Function to get the id of the tile
    def get_id(self):
        return self.tile_id

    def get_colour(self):
        return self.colour


# Class that will define the pattern tile that
class DesignGoalTile:
    def __int__(self, tile_id, requirement):
        self.requirement = requirement
        self.colour_complete = False
        self.pattern_complete = False

        # directions
        self.west = None
        self.east = None
        self.north_west = None
        self.north_east = None
        self.south_east = None
        self.south_west = None

    # We will need different check patterns depending on the requirements

    # Function takes the requirement and then check whether patterns match it
    def check_pattern(self, requirement):
        pass

    # Function that will take requirement and check whether the colour requirement is met
    def check_colour(self):
        pass
