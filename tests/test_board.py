"""Tests for the Board module"""
import unittest
from src import Board


class TestTiles(unittest.TestCase):

    def test_open_positions(self):
        """
        Tests that when we add a tile to the board, that position is removed from
        the open positions array. In this test tile with id 8 is added, so 8 should be
        removed from open positions
        :return:
        """
        board = Board.Board(1)
        board = Board.Board(1)
        board.add_tile(8, "Red", "Dots")
        self.assertFalse(8 in board.open_positions)

    def test_tile_8_is_empty(self):
        """
        Tests that tile 8 has no info in it (is a blank tile)
        :return:
        """
        board = Board.Board(1)
        self.assertEqual(board.board[8].colour, None)

    def test_add_to_tile_8(self):
        """
        Tests that the add tile adds the tile correctly
        :return:
        """
        board = Board.Board(1)
        board.add_tile(8, "Red", "Dots")
        info = board.board[8].colour + board.board[8].pattern
        self.assertEqual(info, "RedDots")

    def test_creating_board(self):
        """
        Tests that the
        :return:
        """
        board = Board.Board(1)
        length = len(board.board)
        msg = "The length is: " + str(length) + "!!"
        self.assertTrue(length == 49, msg)

    def test_get_id(self):
        """
        Tests that we are able to get the ID of a tile.
        :return:
        """
        board = Board.Board(1)
        tile_id = board.board[0].tile_id
        self.assertEqual(tile_id, 0, "The ID produced is:" + str(tile_id))

    # Tests that the east is initialised properly
    def test_navigate_along_east(self):
        """
        Tests that we are able to navigate along the east direction. This means that
        the east connections are correctly initialised.
        :return:
        """
        board = Board.Board(1)
        node = board.board[0]
        hold_id = node.tile_id
        # Go move east through the tiles
        while node.east is not None:
            node = node.east
            hold_id = node.tile_id
        self.assertEqual(hold_id, 6, "The ID produced is: " + str(hold_id))

    # Test that the west connection are correct and can be traversed
    def test_navigate_along_west(self):
        """
        Tests that we are able to move along the west direction. This means that
        the west connections are correctly initialised
        :return:
        """
        board = Board.Board(1)
        node = board.board[48]
        hold_id = node.tile_id
        # Move west until we can no more
        while node.west is not None:
            node = node.west
            hold_id = node.tile_id
        self.assertEqual(hold_id, 42, "The ID produced is: " + str(hold_id))

    def test_purple_borders(self):
        """
        Tests the border for the purple board is drawn correct by iterating over the nodes,
        gathering the colour and pattern and then comparing to make sure it is correctly drawn

        :return: Whether the purple border is drawn correct
        """
        board = Board.Board(1)  # Purple board is 1
        border = [0, 1, 2, 3, 4, 5, 6, 7, 14, 21, 28, 35, 42, 43, 44,
                  45, 46, 47, 48, 41, 34, 27, 20, 13]
        test = ""
        for n in border:
            test += str(board.board[n].colour)
            test += str(board.board[n].pattern)

        correct = "YellowFourRedDotsPurpleFourYellowLeafBlueStripesRedFourGreenDotsBlueFourNavy" \
                  "StripesGreenLeafRedPlantsBlueDotsPurpleLeafYellowFourPurpleStripesNavyLeafGreen" \
                  "FourYellowPlantsPurpleDotsNavyFourGreenStripesRedLeafBlueFourNavyPlants"
        self.assertEqual(test, correct, "Test outputs: " + test)

    def test_adding_button(self):
        """
        Tests to see that a connection of 3 or more tiles with the same colour, results
        in a button being added to the button dictionary
        :return:
        """



if __name__ == '__main__':
    unittest.main()
