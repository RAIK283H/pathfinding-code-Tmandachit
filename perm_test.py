import unittest
from permutation import generate_permutations, find_hamiltonian_cycles, is_hamiltonian_cycle
from graph_data import graph_data

class TestPermutationFunctions(unittest.TestCase):

    def test_sjt_permutations(self):
        perms = generate_permutations(3)
        expected = [[1, 2, 3], [1, 3, 2], [3, 1, 2], [3, 2, 1], [2, 3, 1], [2, 1, 3]]
        self.assertEqual(perms, expected, "SJT permutations failed for n=3")

    def test_hamiltonian_cycle_exists(self):
        graph_with_cycle = graph_data[0]
        permutations = generate_permutations(len(graph_with_cycle) - 1)
        result = find_hamiltonian_cycles(permutations, graph_with_cycle)
        self.assertNotEqual(result, -1, "Expected Hamiltonian cycle but found none")

    def test_no_hamiltonian_cycle(self):
        graph_without_cycle = graph_data[1] 
        permutations = generate_permutations(len(graph_without_cycle) - 1)
        result = find_hamiltonian_cycles(permutations, graph_without_cycle)
        self.assertEqual(result, -1, "Expected no Hamiltonian cycle but found one")

if __name__ == '__main__':
    unittest.main()
