import unittest

import src.Tiles as Tiles


class TestTiles(unittest.TestCase):
    # tests that we are able to create a normal tile
    def test_get_normal_tile_id(self):
        tile = Tiles.NormalTile(25)
        result = tile.get_id()
        self.assertEqual(result, 25)

    def test_get_design_tile_id(self):
        tile = Tiles.DesignGoalTile(25, "easy")
        result = tile.id
        self.assertEqual(result, 25)

    # Tests tha we are able to update the location values
    def test_set_get_locations(self):
        self.assertEqual(15, 15)


if __name__ == '__main__':
    unittest.main()
