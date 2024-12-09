from f_w import adjacency_list_to_matrix, floyd_warshall, reconstruct_path
from graph_data import graph_data, shortest_paths

# Convert graph_data to adjacency list format
def process_graph_data(graph_data):
    processed_graphs = []
    for graph in graph_data:
        adj_list = {}
        for i, (_, neighbors) in enumerate(graph):
            adj_list[i] = [(neighbor, 1) for neighbor in neighbors]  # Default weight = 1
        processed_graphs.append(adj_list)
    return processed_graphs

# Verify paths
def verify_paths(graph_data, graph, shortest_paths):
    n = len(graph)
    adj_matrix = adjacency_list_to_matrix(graph, n)
    dist, parent = floyd_warshall(adj_matrix)

    print("\nGraph:")
    for node, (coords, neighbors) in enumerate(graph_data):
        print(f"Node {node}: Coordinates={coords}, Neighbors={neighbors}")

    print("\nShortest Path Results:")
    for i, path in enumerate(shortest_paths):
        start, end = path[0], path[-1]
        shortest_path = reconstruct_path(parent, start, end)
        print(f"Test Path {i+1}: Expected {path}, Computed {shortest_path}")
        if shortest_path == path:
            print(f"Test Path {i+1} PASSED")
        else:
            print(f"Test Path {i+1} FAILED")

if __name__ == "__main__":
    processed_graphs = process_graph_data(graph_data)

    for i, (original_graph, processed_graph, path) in enumerate(zip(graph_data, processed_graphs, shortest_paths)):
        print(f"\nProcessing Graph {i+1}")
        verify_paths(original_graph, processed_graph, [path])

