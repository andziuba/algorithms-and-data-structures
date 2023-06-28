"""
The program creates a table of edges for a graph and performs the following operations on this graph representation:
* Breadth-first search (BFS) for traversing a graph
* Depth-first search (DFS) for traversing a graph
* Kahn's algorithm for topological sorting
* Tarjan's algorithm for topological sorting
"""
from generate_graph import *
from tabulate import tabulate


# Creates a list of edges from given adjacency matrix
def list_of_edges(n, adjacency_matrix):
    edges_list = []

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                edges_list.append([i + 1, j + 1])

    return edges_list


def display_table_of_edges(edges_list):
    print(tabulate(edges_list, headers=["in", "out"], tablefmt="simple_outline"))


def table_of_edges_bfs(vertices, edges_list):
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
                    for edge in edges_list:
                        if edge[0] == current and not visited[edge[1]]:
                            queue.append(edge[1])

    return bfs_order


def table_of_edges_dfs(vertices, edges_list):
    visited = {v: 0 for v in vertices}

    dfs_order = []

    def dfs(current):
        visited[current] = 1
        dfs_order.append(current)
        for edge in edges_list:
            if edge[0] == current and not visited[edge[1]]:
                dfs(edge[1])

    for v in visited:
        if visited[v] == 0:
            dfs(v)

    return dfs_order


def table_of_edges_kahns_algorithm(vertices, edges_list):
    in_degrees = {v: 0 for v in vertices}

    for i, j in edges_list:
        in_degrees[j] += 1

    in_degree_0 = []
    for vertex, degree in in_degrees.items():
        if degree == 0:
            in_degree_0.append(vertex)

    result = []
    while in_degree_0:
        u = in_degree_0.pop(0)
        result.append(u)
        for edge in edges_list:
            if edge[0] == u:
                v = edge[1]
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    in_degree_0.append(v)

    return result


def table_of_edges_tarjans_algorithm(vertices, edges_list):
    visited = {v: "white" for v in vertices}  # White - not visited

    stack = []

    def dfs(current):
        visited[current] = "gray"  # Gray - currently processing

        for edge in edges_list:
            if edge[0] == current:
                if visited[edge[1]] == "white":
                    dfs(edge[1])

        visited[current] = "black"  # Black - done
        stack.append(current)

    for v in visited:
        if visited[v] == "white":
            dfs(v)

    return stack[::-1]


num_of_vertices = int(input("Enter number of vertices: "))
adj_matrix = generate_graph(num_of_vertices)
vertices_list = [i + 1 for i in range(num_of_vertices)]

edges = list_of_edges(num_of_vertices, adj_matrix)
print("Table of edges:")
display_table_of_edges(edges)

bfs = table_of_edges_bfs(vertices_list, edges)
print("\nBFS order:", *bfs)

dfs = table_of_edges_dfs(vertices_list, edges)
print("DFS order:", *dfs)

sorted_kahns = table_of_edges_kahns_algorithm(vertices_list, edges)
print("Topological sort using Kahn's algorithm:", *sorted_kahns)

sorted_tarjans = table_of_edges_tarjans_algorithm(vertices_list, edges)
print("Topological sort using Tarjan's algorithm:", *sorted_tarjans)
