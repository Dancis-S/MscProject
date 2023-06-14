"""Classes that define the tiles that will be used in the game"""


# Class to define the tile object that will be used to represent the nodes in the board
class NormalTile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.pattern = None
        self.colour = None
        self.part_of_pattern = False

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
        colour_complete = False
        pattern_complete = False
        neighbors = self.get_neighbors()
        for n in neighbors:
            pass  # We need to check that no other tile is equal

    def aaa_bbb_goal(self):
        """
        
        :return:
        """
        pass

    def aa_bb_cc_goal(self):
        """

        :return:
        """
        pass

    def aaaa_bb_goal(self):
        """

        :return:
        """
        pass

    def aaa_bb_c_goal(self):
        """

        :return:
        """
        pass

    def aa_bb_c_d_goal(self):
        """

        :return:
        """
        pass

    def get_neighbors(self):
        """
        Function that gets all the neighboring nodes and returns them in an array. The
        order is W, NW, NE, E, SE, SW
        :return: Array containing tile neighbors in order W, NW, NE, E, SE, SW
        """
        return [self.west, self.north_west, self.north_east, self.east, self.south_east, self.south_west]
