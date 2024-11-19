import math
import unittest

import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path, get_dijkstra_path


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

    def test_dijkstra_path(self):
        path = get_dijkstra_path()
        self.assertIn(3, path, "The path should include the target node 3.")
        self.assertEqual(path[-1], 4, "The path should end at the exit node 4.")
        self.assertTrue(self.validate_path(path), "The path should consist of valid edges.")
    
    def test_disconnected_graph(self):
        graph_data.graph_data = [
            [
                [(0, 0), {1: 1}],
                [(100, 0), {0: 1}],
                [(0, 100), {}],  # Node 2 is disconnected
                [(100, 100), {4: 1}],
                [(200, 200), {}]
            ]
        ]
        global_game_data.target_node = [3]
        
        with self.assertRaises(AssertionError, msg="No path should exist in a disconnected graph."):
            get_dijkstra_path()
            
    def test_cyclic_graph(self):
        graph_data.graph_data = [
            [
                [(0, 0), {1: 1}],
                [(100, 0), {0: 1, 2: 1}],
                [(0, 100), {1: 1, 3: 1}],
                [(100, 100), {2: 1, 4: 1}],
                [(200, 200), {3: 1}]
            ]
        ]
        global_game_data.target_node = [3]
        
        path = get_dijkstra_path()
        self.assertIn(3, path, "The path should include the target node 3.")
        self.assertEqual(path[-1], 4, "The path should end at the exit node 4.")
        self.assertTrue(self.validate_path(path), "The path should consist of valid edges.")
        
    def test_multiple_equal_weight_paths(self):
        graph_data.graph_data = [
            [
                [(0, 0), {1: 1, 2: 1}],
                [(100, 0), {0: 1, 3: 1}],
                [(0, 100), {0: 1, 3: 1}],
                [(100, 100), {1: 1, 2: 1, 4: 1}],
                [(200, 200), {}]
            ]
        ]
        global_game_data.target_node = [3]
        
        path = get_dijkstra_path()
        self.assertIn(3, path, "The path should include the target node 3.")
        self.assertEqual(path[-1], 4, "The path should end at the exit node 4.")
        self.assertTrue(self.validate_path(path), "The path should consist of valid edges.")
        
    def test_single_node_graph(self):
        graph_data.graph_data = [
            [
                [(0, 0), {}]
            ]
        ]
        global_game_data.target_node = [0]
        
        path = get_dijkstra_path()
        self.assertEqual(path, [0], "The path should only contain the single node in the graph.")
        
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
        
    def validate_path(self, path):
        graph = graph_data.graph_data[global_game_data.current_graph_index]
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]][1]:
                return False
        return True


if __name__ == '__main__':
    unittest.main()
