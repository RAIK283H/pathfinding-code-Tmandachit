import math
import unittest

import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def setUp(self):
        # Setup the common graph data for all tests
        global_game_data.current_graph_index = 0
        graph_data.graph_data = [
            [
                [(0, 0), [1, 2]],
                [(100, 0), [0, 3]],
                [(0, 100), [0, 3]],
                [(100, 100), [1, 2, 4]],
                [(200, 200), []]
            ]
        ]
        global_game_data.target_node = [3]

    def test_dfs_path(self):
        # Test the DFS path from start to target to exit
        path = get_dfs_path()
        self.assertIn(3, path, "The path should include the target node 3.")
        self.assertEqual(path[-1], 4, "The path should end at the exit node 4.")

    def test_bfs_path(self):
        # Test the BFS path from start to target to exit
        path = get_bfs_path()
        self.assertIn(3, path, "The path should include the target node 3.")
        self.assertEqual(path[-1], 4, "The path should end at the exit node 4.")


if __name__ == '__main__':
    unittest.main()
