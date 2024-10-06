import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    # Get the grapgh and node data
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1
    
    # Pre Condition: Must have atleast 2 nodes start end and target
    assert len(graph) >= 2, "The graph must have at least two nodes."
    
    # Helper function to generate random path between two nodes
    def random_path_between(current_node, target_node, visited):
        path = []
        while current_node != target_node:
            neighbors = [n for n in graph[current_node][1] if n not in visited]
            if not neighbors:
                return None
            next_node = random.choice(neighbors)
            path.append(int(next_node))
            visited.add(int(next_node))
            current_node = next_node
        return path

    # Generate the path
    visited = set()
    visited.add(start_node)
    
    start_to_target_path = random_path_between(start_node, target_node, visited)
    target_to_exit_path = random_path_between(target_node, exit_node, visited)
    if start_to_target_path == None or target_to_exit_path == None:
        return "Random Path Generator failed"
    
    full_path = start_to_target_path + target_to_exit_path  

    # Postcondition: Must include target and end at exit
    assert start_node in visited, "Path must start at the start node"
    assert target_node in full_path, "Path must include the target node."
    assert full_path[-1] == exit_node, "Path must end at the exit node."

    return full_path

def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
