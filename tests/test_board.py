"""Tests for the Board module"""
import unittest
import src.Board as Board


class TestTiles(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(1, 1)

    def test_creating_board(self):
        board = Board.Board(1)
        first_tile_id = board.board[0].id
        self.assertEqual(first_tile_id, 0)


if __name__ == '__main__':
    unittest.main()
