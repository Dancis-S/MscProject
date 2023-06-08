"""Tests for the Tiles module"""
import unittest
from src import Tiles
from src import Board

class TestTiles(unittest.TestCase):
    # Tests that we are able to create a normal tile
    def test_get_normal_tile_id(self):
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
        board = Board.Board(1)
        board.add_tile(9, "Red", "Dots")
        board.add_tile(10, "Red", "Dots")
        board.add_tile(18, "Red", "Dots")
        board.add_tile(24, "Red", "Dots")
        board.add_tile(16, "Red", "Dots")
        complete = board.board[17].check_tile_complete()
        self.assertFalse(complete, "It returns: " + str(complete))

    # Tests that you can get a tiles id
    def test_get_design_tile_id(self):
        tile = Tiles.DesignGoalTile(25, "easy")
        result = tile.id
        self.assertEqual(result, 25)

    # Tests that you're able to access the neighbor tile
    def test_set_get_locations(self):
        tile = Tiles.NormalTile(25)
        neighbor = Tiles.NormalTile(11)
        tile.north_east = neighbor
        self.assertEqual(tile.north_east.tile_id, 11)

    # Tests that you can get/set colour + pattern property
    def test_properties_normal_tile(self):
        tile = Tiles.NormalTile(25)
        tile.pattern = "Stripes"
        tile.colour = "Purple"
        self.assertEqual(tile.pattern, "Stripes") and \
        self.assertEqual(tile.colour, "Purple")


if __name__ == '__main__':
    unittest.main()
