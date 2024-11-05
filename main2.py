from graph_data import graph_data
from permutation import generate_permutations, find_hamiltonian_cycles
import random

def setup_graphs():
    target_nodes = []
    for graph in graph_data:
        if len(graph) >= 3:
            target_nodes.append(random.randint(1, len(graph) - 2))
        else:
            target_nodes.append(0)
    return target_nodes

def main():
    target_nodes = setup_graphs()
    
    for i, graph in enumerate(graph_data):
        print(f"\nProcessing graph {i+1} with target nodes: {target_nodes[i]}")
        
        permutations = generate_permutations(len(graph) - 1)
        
        hamiltonian_cycles = find_hamiltonian_cycles(permutations, graph)
        
        if hamiltonian_cycles == -1:
            print("No valid Hamiltonian cycle found.")
            print(-1)
        else:
            print("Valid Hamiltonian Cycles:")
            for cycle in hamiltonian_cycles:
                print(cycle)
                
if __name__ == '__main__':
    main()
