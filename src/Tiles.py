"""Classes that define the tiles that will be used in the game"""


# Class to define the tile object that will be used to represent the nodes in the board
class NormalTile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.pattern = None
        self.colour = None
        self.part_of_pattern = False
        self.part_of_button = False  # Used for buttons

        # Neighbors
        self.west = None
        self.east = None
        self.north_west = None
        self.north_east = None
        self.south_east = None
        self.south_west = None

    def get_id(self):
        """
        Gets the current tiles ID
        :return:
        """
        return self.tile_id

    def get_neighbors(self):
        """
        Function that gets all the neighboring nodes and returns them in an array. The
        order is W, NW, NE, E, SE, SW
        :return: Array containing tile neighbors in order W, NW, NE, E, SE, SW
        """
        return [self.west, self.north_west, self.north_east, self.east, self.south_east, self.south_west]


class DesignGoalTile:
    def __init__(self, tile_id, requirement):
        self.requirement = requirement
        self.colour_complete = False
        self.pattern_complete = False
        self.id = tile_id

        # Neighbors
        self.west = None
        self.east = None
        self.north_west = None
        self.north_east = None
        self.south_east = None
        self.south_west = None

    # We will need different check patterns depending on the requirements

    def check_tile_complete(self):
        """
        Checks that the design tile is completed (all 6 sides are connected to another
        tile). This is called before running code that checks the given requirements are met
        for scoring
        :return: Returns True if design tile is fully connected otherwise False
        """
        neighbors = self.get_neighbors()
        completed = True
        for n in neighbors:
            if n.colour is None or n.pattern is None:
                completed = False
                break

        return completed

    def check_design_goal_reached(self, requirement):
        """
        Given the tiles requirements, check that is has been completed with patterns, or
        with colours
        :param requirement:
        :return:
        """
        pass

    def not_equal_goal(self):
        """
        Checks that all the neighbors are different for the tile which requires all colours
        and patterns to be different.
        :return:
        """
        colour_complete = True
        pattern_complete = True
        colours = []
        patterns = []
        neighbors = self.get_neighbors()
        for n in neighbors:
            # Check that the colour hasn't already been seen
            if n.colour in colours:
                colour_complete = False
            else:
                colours.append(n.colour)

            if n.pattern in patterns:
                pattern_complete = False
            else:
                patterns.append(n.pattern)

        # Returns scoring based on conditions met
        if colour_complete and pattern_complete:
            return 10
        elif colour_complete or pattern_complete:
            return 6
        else:
            return 0

    def add_colours_and_patterns_to_dictionary(self):
        """
        Function that will get the colour and pattern of all the surrounding tiles, add them
        to their respective dictionaries, and then return the colour and pattern dictionary.
        Used when needing to check the design tiles conditions are met
        :return:
        Returns first colours then pattern dictionaries
        """
        neighbors = self.get_neighbors()
        colours_dict = {}
        patterns_dict = {}

        for n in neighbors:  # Loops and add them to dictionary
            if n.colour in colours_dict:
                colours_dict[n.colour] += 1
            else:
                colours_dict[n.colour] = 1
            if n.pattern in patterns_dict:
                patterns_dict[n.pattern] += 1
            else:
                patterns_dict[n.pattern] = 1

        return colours_dict, patterns_dict

    def aaa_bbb_goal(self):
        """
        Checks that there are only 2 groups with each of size 3, for colour and pattern.
        :return:
        """
        colour_complete, pattern_complete = False
        colours_dict, patterns_dict = self.add_colours_and_patterns_to_dictionary()

        # Check that the dictionaries meet the conditions
        colour_keys = list(colours_dict.keys())
        pattern_keys = list(patterns_dict.keys())
        if len(colours_dict) == 2 and len(colour_keys[0]) == 3 and len(colour_keys[1] == 3):
            colour_complete = True
        if len(patterns_dict) == 2 and len(pattern_keys[0]) == 3 and len(pattern_keys[1]) == 3:
            pattern_complete = True

        # Return the score depending on the requirements met
        if pattern_complete and colour_complete:
            return 10
        elif pattern_complete or colour_complete:
            return 6
        else:
            return 0

    def aa_bb_cc_goal(self):
        """
        Checks that the design tile has 3 different groups (colour or pattern), with each
        of length 2. i.e. 2 red, 2 green, 2 blue tiles surrounding it
        :return:
        """
        colour_complete, pattern_complete = False
        colours_dict, patterns_dict = self.add_colours_and_patterns_to_dictionary()

        # Check that the dictionaries meet the conditions
        colour_keys = list(colours_dict.keys())
        pattern_keys = list(patterns_dict.keys())
        if len(colours_dict) == 3 and len(colour_keys[0]) == 2 and len(colour_keys[1] == 2) \
                and len(colour_keys[2] == 2):
            colour_complete = True
        if len(patterns_dict) == 3 and len(pattern_keys[0]) == 2 and len(pattern_keys[1]) == 2 \
                and len(pattern_keys[2]) == 2:
            pattern_complete = True

        # Return the score depending on the requirements met
        if pattern_complete and colour_complete:
            return 10
        elif pattern_complete or colour_complete:
            return 6
        else:
            return 0

    def aaaa_bb_goal(self):
        """
        Design requirement where there are 2 groups (pattern or colour group), one with size 4 and
        other with the size 2
        :return:
        """
        colour_complete, pattern_complete = False
        colours_dict, patterns_dict = self.add_colours_and_patterns_to_dictionary()

        # Check that they meet the conditions
        colour_values = list(colours_dict.values())
        pattern_values = list(patterns_dict.values())

        if len(colour_values) == 2 and 4 in colours_dict and 2 in colours_dict:
            colour_complete = True
        if len(pattern_values) == 2 and 4 in patterns_dict and 2 in patterns_dict:
            pattern_complete = True

        # Returns scores based on the conditions met
        if pattern_complete and colour_complete:
            return 10
        elif pattern_complete or colour_complete:
            return 6
        else:
            return 0

    def aaa_bb_c_goal(self):
        """

        :return:
        """
        colour_complete, pattern_complete = False
        colours_dict, patterns_dict = self.add_colours_and_patterns_to_dictionary()

        # Check that they meet the conditions
        colour_values = list(colours_dict.values())
        pattern_values = list(patterns_dict.values())

        if len(colour_values) == 3 and 3 in colour_values and 2 in colour_values and 1 in colour_values:
            colour_complete = True
        if len(pattern_values) == 3 and 3 in pattern_values and 2 in pattern_values and 1 in pattern_values:
            pattern_complete = True

        # Returns scores based on the conditions met
        if pattern_complete and colour_complete:
            return 10
        elif pattern_complete or colour_complete:
            return 6
        else:
            return 0

    def aa_bb_c_d_goal(self):
        """

        :return:
        """
        colour_complete, pattern_complete = False
        colours_dict, patterns_dict = self.add_colours_and_patterns_to_dictionary()

        # Check that they meet the conditions
        colour_values = list(colours_dict.values())
        pattern_values = list(patterns_dict.values())

        # Check that the outlined conditions are met
        if len(colour_values) == 4 and colour_values.count(2) == 2 and colour_values.count(1) == 2:
            colour_complete = True
        if len(pattern_values) == 4 and pattern_values.count(2) == 2 and pattern_values.count(1) == 1:
            pattern_complete = True

        # Returns scores based on the conditions met
        if pattern_complete and colour_complete:
            return 10
        elif pattern_complete or colour_complete:
            return 6
        else:
            return 0

    def get_neighbors(self):
        """
        Function that gets all the neighboring nodes and returns them in an array. The
        order is W, NW, NE, E, SE, SW
        :return: Array containing tile neighbors in order W, NW, NE, E, SE, SW
        """
        return [self.west, self.north_west, self.north_east, self.east, self.south_east, self.south_west]
