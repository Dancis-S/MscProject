"""Tests for the Board module"""
import unittest
import src.Board as Board


class TestTiles(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)

    def test_creating_board(self):
        board = Board.Board(1)
        length = len(board.board)
        msg = "The length is: " + str(length) + "!!"
        self.assertTrue(length == 49, msg)

    def test_get_id(self):
        board = Board.Board(1)
        tile_id = board.board[0].tile_id
        self.assertEqual(tile_id, 0)


if __name__ == '__main__':
    unittest.main()
