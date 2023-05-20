# Code the Represents the Calico board

# Class to define the tile object that will be used to represent the nodes in the board
class NormalTile:
    def __init__(self, tile_id, pattern, colour, west, north_west, north_east, east, south_east, south_west):
        self.tile_id = tile_id
        self.pattern = pattern
        self.colour = colour

        # directions
        self.west = west
        self.east = east
        self.north_west = north_west
        self.north_east = north_east
        self.south_east = south_east
        self.south_west = south_west


# Class that will define the pattern tile that
class DesignGoalTile:
    def __int__(self, requirement, west, north_west, north_east, east, south_east, south_west):
        self.requirement = requirement
        self.colour_complete = False
        self.pattern_complete = False

        # directions
        self.west = west
        self.east = east
        self.north_west = north_west
        self.north_east = north_east
        self.south_east = south_east
        self.south_west = south_west

    # We will need different check patterns depending on the requirements

    # Function takes the requirement and then check whether patterns match it
    def check_pattern(self, requirement):
        pass

    # Function that will take requirement and check whether the colour requirement is met
    def check_colour(self):
        pass
