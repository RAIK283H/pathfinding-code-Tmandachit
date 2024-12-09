import unittest
from f_w import adjacency_list_to_matrix, floyd_warshall, reconstruct_path


class TestFloydWarshall(unittest.TestCase):
    def test_adjacency_list_to_matrix(self):
        adj_list = {
            0: [(1, 3), (2, 8)],
            1: [(3, 1)],
            2: [(3, 1)],
            3: []
        }
        expected_matrix = [
            [0, 3, 8, float('inf')],
            [float('inf'), 0, float('inf'), 1],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0],
        ]
        result = adjacency_list_to_matrix(adj_list, 4)
        self.assertEqual(result, expected_matrix)

    
    def test_reconstruct_path_basic(self):
        matrix = [
            [0, 3, float('inf'), float('inf')],
            [float('inf'), 0, 1, 7],
            [float('inf'), float('inf'), 0, 2],
            [6, float('inf'), float('inf'), 0],
        ]
        _, parent = floyd_warshall(matrix)
        self.assertEqual(reconstruct_path(parent, 0, 3), [0, 1, 2, 3])
        self.assertEqual(reconstruct_path(parent, 3, 1), [3, 0, 1])
        self.assertEqual(reconstruct_path(parent, 0, 0), [0])

    def test_single_node_graph(self):
        adj_list = {
            0: []
        }
        matrix = adjacency_list_to_matrix(adj_list, 1)
        dist, parent = floyd_warshall(matrix)
        self.assertEqual(dist, [[0]])
        self.assertEqual(reconstruct_path(parent, 0, 0), [0])

    def test_disconnected_graph(self):
        adj_list = {
            0: [(1, 5)],
            1: [],
            2: [(3, 1)],
            3: []
        }
        matrix = adjacency_list_to_matrix(adj_list, 4)
        dist, parent = floyd_warshall(matrix)
        self.assertEqual(dist, [
            [0, 5, float('inf'), float('inf')],
            [float('inf'), 0, float('inf'), float('inf')],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0],
        ])
        self.assertEqual(reconstruct_path(parent, 0, 1), [0, 1])
        self.assertEqual(reconstruct_path(parent, 0, 3), [])
        self.assertEqual(reconstruct_path(parent, 2, 3), [2, 3])

    def test_negative_weights(self):
        adj_list = {
            0: [(1, 4), (2, -2)],
            1: [(3, 3)],
            2: [(1, 1), (3, 2)],
            3: []
        }
        matrix = adjacency_list_to_matrix(adj_list, 4)
        dist, parent = floyd_warshall(matrix)
        self.assertEqual(dist, [
            [0, -1, -2, 0],
            [float('inf'), 0, float('inf'), 3],
            [float('inf'), 1, 0, 2],
            [float('inf'), float('inf'), float('inf'), 0],
        ])
        self.assertEqual(reconstruct_path(parent, 0, 3), [0, 2, 3])
        self.assertEqual(reconstruct_path(parent, 1, 2), [])
        self.assertEqual(reconstruct_path(parent, 0, 2), [0, 2])


if __name__ == "__main__":
    unittest.main()
