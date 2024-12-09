import graph_data
import global_game_data
import heapq
from numpy import random
from collections import deque

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())

def get_test_path():
    return graph_data.shortest_paths[global_game_data.current_graph_index]


def get_random_path():
    # Get the graph and node data
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1
    
    # Precondition: Must have at least 2 nodes (start, end, and target)
    assert len(graph) >= 2, "The graph must have at least two nodes."
    
    # Helper function to generate random path between two nodes
    def random_path_between(current_node, target_node, visited):
        while True:
            path = [int(current_node)]  # Convert current_node to Python int
            while current_node != target_node:
                neighbors = [int(n) for n in graph[current_node][1] if n not in visited]  # Convert neighbors to Python int
                if not neighbors:
                    break
                next_node = random.choice(neighbors)
                path.append(int(next_node))  # Convert next_node to Python int
                visited.add(int(next_node))  # Add as Python int
                current_node = next_node
            if current_node == target_node:
                return path[1:]
            visited.clear()
            visited.add(start_node)

    # Generate the path
    visited = set()
    visited.add(start_node)
    
    start_to_target_path = random_path_between(start_node, target_node, visited)
    target_to_exit_path = random_path_between(target_node, exit_node, visited)
    
    full_path = start_to_target_path + target_to_exit_path

    # Postcondition: Must include target and end at exit
    assert target_node in full_path, "Path must include the target node."
    assert full_path[-1] == exit_node, "Path must end at the exit node."

    return full_path

def get_dfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1

    def dfs(start, target):
        stack = [(start, [start])]
        visited = set()
        while stack:
            current_node, path = stack.pop()
            if current_node == target:
                return path
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in graph[current_node][1]:
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        return None

    start_to_target_path = dfs(start_node, target_node)
    target_to_exit_path = dfs(target_node, exit_node)

    assert start_to_target_path is not None and target_to_exit_path is not None, "DFS failed to find a valid path."
    full_path = start_to_target_path[1:] + target_to_exit_path[1:]

    assert target_node in full_path, "Path must include the target node."
    assert full_path[-1] == exit_node, "Path must end at the exit node."

    return full_path

def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1

    def bfs(start, target):
        queue = deque([[start]])
        visited = set([start])
        while queue:
            path = queue.popleft()
            current_node = path[-1]
            if current_node == target:
                return path
            for neighbor in graph[current_node][1]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])
        return None

    start_to_target_path = bfs(start_node, target_node)
    target_to_exit_path = bfs(target_node, exit_node)

    assert start_to_target_path is not None and target_to_exit_path is not None, "BFS failed to find a valid path."
    full_path = start_to_target_path[1:] + target_to_exit_path[1:]

    assert target_node in full_path, "Path must include the target node."
    assert full_path[-1] == exit_node, "Path must end at the exit node."

    return full_path


def get_dijkstra_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    start_node = 0
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node = len(graph) - 1

    def dijkstra(start, target):
        # Priority queue with (cost, node, path)
        priority_queue = []
        heapq.heappush(priority_queue, (0, start, [start]))

        # Distance dictionary to store the shortest distance to each node
        shortest_distances = {start: 0}

        while priority_queue:
            current_cost, current_node, current_path = heapq.heappop(priority_queue)

            # Stop if we reach the target
            if current_node == target:
                return current_path

            # Check neighbors (assume weights are all 1 for simplicity or adapt as needed)
            for neighbor in graph[current_node][1]:
                new_cost = current_cost + 1  # Replace 1 with the actual weight if weights are stored elsewhere
                if neighbor not in shortest_distances or new_cost < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor, current_path + [neighbor]))

        return None


    # Find the path from start to target
    start_to_target_path = dijkstra(start_node, target_node)
    assert start_to_target_path is not None, "No path found from start to target."

    # Find the path from target to exit
    target_to_exit_path = dijkstra(target_node, exit_node)
    assert target_to_exit_path is not None, "No path found from target to exit."

    # Combine the paths (avoiding duplicate target node)
    full_path = start_to_target_path[:-1] + target_to_exit_path

    # Postconditions
    assert full_path[0] == start_node, "Path must start at the start node."
    assert full_path[-1] == exit_node, "Path must end at the exit node."
    assert target_node in full_path, "Path must include the target node."

    return full_path