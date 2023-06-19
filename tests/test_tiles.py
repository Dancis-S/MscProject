"""Tests for the Tiles module"""
import unittest
from src import Tiles
from src import Board


class TestTiles(unittest.TestCase):
    # Tests that we are able to create a normal tile
    def test_get_normal_tile_id(self):
        """
        Tests the get id function for normal tiles
        :return:
        """
        tile = Tiles.NormalTile(25)
        result = tile.get_id()
        self.assertEqual(result, 25)

    def test_tile_complete_test(self):
        """
        Tests that the function that checks that design tile is complete works
        :return: Passes if all tile and present otherwise fails
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Dots")
        board.add_tile(18, "Red", "Dots")
        board.add_tile(24, "Red", "Dots")
        board.add_tile(16, "Red", "Dots")
        board.add_tile(23, "Red", "Dots")
        self.assertTrue(board.board[17].check_tile_complete())

    def test_tile_complete_test_is_incomplete(self):
        """

        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Dots")
        board.add_tile(18, "Red", "Dots")
        board.add_tile(24, "Red", "Dots")
        board.add_tile(16, "Red", "Dots")
        complete = board.board[17].check_tile_complete()
        self.assertFalse(complete, "It returns: " + str(complete))

    def test_get_design_tile_id(self):
        """
        Tests that we can set the tiles ID
        :return:
        """
        tile = Tiles.DesignGoalTile(25, "easy")
        result = tile.id
        self.assertEqual(result, 25)

    def test_set_get_locations(self):
        """
        Tests that we are able to access the neighboring tile
        :return:
        """
        tile = Tiles.NormalTile(25)
        neighbor = Tiles.NormalTile(11)
        tile.north_east = neighbor
        self.assertEqual(tile.north_east.tile_id, 11)

    def test_properties_normal_tile(self):
        """
        Tests that we can correctly set the properties of the default tiles
        :return:
        """
        tile = Tiles.NormalTile(25)
        tile.pattern = "Stripes"
        tile.colour = "Purple"
        combined = tile.colour + tile.pattern
        self.assertEqual(combined, "PurpleStripes")

    def test_not_equal_goal_1(self):
        """
        Checks that the design goal tile works correctly in the case where they are all
        different
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Blue", "Leaf")
        board.add_tile(18, "Navy", "Stripes")
        board.add_tile(24, "Yellow", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Purple", "Flowers")
        score = board.board[17].not_equal_goal()
        self.assertEqual(score, 15)

    def test_not_equal_goal_2(self):
        """
        Tests in scenario where only colour is completed not pattern
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Blue", "Leaf")
        board.add_tile(18, "Navy", "Stripes")
        board.add_tile(24, "Yellow", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Purple", "Leaf")
        score = board.board[17].not_equal_goal()
        self.assertEqual(score, 10)

    def test_not_equal_goal_3(self):
        """
        Tests for scenario where only pattern is completed
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Blue", "Leaf")
        board.add_tile(18, "Navy", "Stripes")
        board.add_tile(24, "Yellow", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Flowers")
        score = board.board[17].not_equal_goal()
        self.assertEqual(score, 10)

    def test_not_equal_goal_4(self):
        """
        Tests where none of them are properly completed
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Blue", "Leaf")
        board.add_tile(18, "Navy", "Stripes")
        board.add_tile(24, "Yellow", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Dots")
        score = board.board[17].not_equal_goal()
        self.assertEqual(score, 0)

    def test_aaa_bbb_1(self):
        """
        Tests for scenario where design tile is completed both in colour and in pattern.
        It is required that there are only 2 groups with the length of 3, i.e. aaa-bbb
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Leaf")
        board.add_tile(18, "Red", "Stripes")
        board.add_tile(24, "Green", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Flowers")
        score = board.board[17].aaa_bbb_goal()
        self.assertEqual(score, 13)

    def test_aaa_bbb_2(self):
        """
        Tests for scenario where design tile is only colour completed. It is required
        that there are only 2 groups with the length of 3, i.e. aaa-bbb
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Leaf")
        board.add_tile(18, "Red", "Stripes")
        board.add_tile(24, "Green", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Flowers")
        score = board.board[17].aaa_bbb_goal()
        self.assertEqual(score, 7)

    def test_aaa_bbb_3(self):
        """
        Tests for scenario where design tile is only pattern completed. It is required
        that there are only 2 groups with the length of 3, i.e. aaa-bbb
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Leaf")
        board.add_tile(18, "Red", "Stripes")
        board.add_tile(24, "Green", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Flowers")
        score = board.board[17].aaa_bbb_goal()
        self.assertEqual(score, 7)

    def test_aaa_bbb_4(self):
        """
        Tests for scenario where neither the colour nor pattern condition is met. It is required
        that there are only 2 groups with the length of 3, i.e. aaa-bbb
        :return:
        """
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Leaf")
        board.add_tile(18, "Red", "Stripes")
        board.add_tile(24, "Green", "Plants")
        board.add_tile(23, "Green", "Four")
        board.add_tile(16, "Green", "Flowers")
        score = board.board[17].aaa_bbb_goal()
        self.assertEqual(score, 0)


if __name__ == '__main__':
    unittest.main()
