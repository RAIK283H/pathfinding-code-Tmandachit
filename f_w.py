def adjacency_list_to_matrix(adj_list, n, inf=float('inf')):
    matrix = [[inf] * n for _ in range(n)]
    for u in range(n):
        matrix[u][u] = 0 
        for v, weight in adj_list[u]:
            matrix[u][v] = weight
    return matrix

def floyd_warshall(matrix):
    n = len(matrix)
    dist = [row[:] for row in matrix]  # Copy input matrix
    parent = [[None if matrix[i][j] == float('inf') else i for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]  # Update parent matrix
    return dist, parent


def reconstruct_path(parent, start, end):
    if parent[start][end] is None:
        return []
    path = []
    while end != start:
        path.append(end)
        end = parent[start][end]
    path.append(start)
    return path[::-1] 
