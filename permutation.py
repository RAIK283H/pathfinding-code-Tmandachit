def generate_permutations(n):
    permutation = list(range(1, n + 1))
    directions = [-1] * n
    result = [permutation[:]]

    while True:
        index = -1
        value = -1
        for i in range(n):
            if directions[i] == -1 and i > 0 and permutation[i] > permutation[i - 1]:
                if permutation[i] > value:
                    value = permutation[i]
                    index = i
            elif directions[i] == 1 and i < n - 1 and permutation[i] > permutation[i + 1]:
                if permutation[i] > value:
                    value = permutation[i]
                    index = i

        if index == -1:
            break

        swap_index = index + directions[index]
        permutation[index], permutation[swap_index] = permutation[swap_index], permutation[index]
        directions[index], directions[swap_index] = directions[swap_index], directions[index]
        index = swap_index

        for i in range(n):
            if permutation[i] > value:
                directions[i] *= -1

        result.append(permutation[:])
        
    return result

def is_hamiltonian_cycle(path, graph):
    # Construct full path by prepending 0 and appending the last node
    full_path = [0] + path + [path[0]]

    print("Full Path:", full_path)
    print("Graph Structure:", graph)
    print("\n")

    # Check each consecutive node in full_path to ensure an edge exists
    for i in range(len(full_path) - 1):
        current_node = full_path[i]
        next_node = full_path[i + 1]

        # Debug output for adjacency check
        print("Adjacency Check between nodes:", current_node, "->", next_node)
        print("Adjacency List of Current Node:", graph[current_node][1])

        # Ensure next_node is in the adjacency list of current_node
        if next_node not in graph[current_node][1]:
            print("Failed adjacency check:", next_node, "is not in", graph[current_node][1])
            return False
        print("Passed adjacency check.\n")

    return True


def find_hamiltonian_cycles(permutations, graph):
    cycles = []
    for path in permutations:
        if is_hamiltonian_cycle(path, graph):
            cycles.append(path)
    return cycles if cycles else -1