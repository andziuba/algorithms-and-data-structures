"""
The program creates an adjacency matrix for a graph and performs the following operations on this graph representation:
* Breadth-first search (BFS) for a graph traversal
* Depth-first search (DFS) for a graph traversal
* Kahn's algorithm for topological sorting
* Tarjan's algorithm for topological sorting
"""
from generate_graph import *
from tabulate import tabulate


def display_adjacency_matrix(n, matrix):
    vertices_l = []
    for i in range(1, n + 1):
        vertices_l.append(str(i))
    print(tabulate(matrix, headers=vertices_l, showindex=vertices_l, tablefmt="simple_outline"))


def adjacency_matrix_bfs(vertices, adjacency_matrix):
    visited = {v: 0 for v in vertices}

    bfs_order = []

    for current in visited:
        if visited[current] == 0:
            queue = [current]
            while queue:
                current = queue.pop(0)
                if not visited[current]:
                    bfs_order.append(current)
                    visited[current] = 1
                    for i in range(len(adjacency_matrix)):
                        if adjacency_matrix[current - 1][i] and not visited[i + 1]:
                            queue.append(i + 1)

    return bfs_order


def adjacency_matrix_dfs(vertices, adjacency_matrix):
    visited = {v: 0 for v in vertices}

    dfs_order = []

    def dfs(current):
        visited[current] = 1
        dfs_order.append(current)
        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[current - 1][i] and not visited[i + 1]:
                dfs(i + 1)

    for v in visited:
        if visited[v] == 0:
            dfs(v)

    return dfs_order


def adjacency_matrix_kahns_algorithm(vertices, adjacency_matrix):
    in_degrees = {v: 0 for v in vertices}

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if adjacency_matrix[i][j]:
                in_degrees[j + 1] += 1

    in_degree_0 = []
    for vertex, degree in in_degrees.items():
        if degree == 0:
            in_degree_0.append(vertex)

    result = []
    while in_degree_0:
        u = in_degree_0.pop(0)
        result.append(u)
        for v in range(len(adjacency_matrix)):
            if adjacency_matrix[u - 1][v] == 1:
                in_degrees[v + 1] -= 1
                if in_degrees[v + 1] == 0:
                    in_degree_0.append(v + 1)

    return result


def adjacency_matrix_tarjans_algorithm(vertices, adjacency_matrix):
    visited = {v: "white" for v in vertices}  # White - not visited

    stack = []

    def dfs(current):
        visited[current] = "gray"  # Gray - currently processing

        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[current - 1][i]:
                if visited[i + 1] == "white":
                    dfs(i + 1)

        visited[current] = "black"  # Black - done
        stack.append(current)

    for v in visited:
        if visited[v] == "white":
            dfs(v)

    return stack[::-1]


num_of_vertices = int(input("Enter number of vertices: "))
adj_matrix = generate_graph(num_of_vertices)
vertices_list = [i + 1 for i in range(num_of_vertices)]

print("Adjacency matrix:")
display_adjacency_matrix(num_of_vertices, adj_matrix)

bfs = adjacency_matrix_bfs(vertices_list, adj_matrix)
print("\nBFS order:", *bfs)

dfs = adjacency_matrix_dfs(vertices_list, adj_matrix)
print("DFS order:", *dfs)

sorted_kahns = adjacency_matrix_kahns_algorithm(vertices_list, adj_matrix)
print("Topological sort using Kahn's algorithm:", *sorted_kahns)

sorted_tarjans = adjacency_matrix_tarjans_algorithm(vertices_list, adj_matrix)
print("Topological sort using Tarjan's algorithm:", *sorted_tarjans)
