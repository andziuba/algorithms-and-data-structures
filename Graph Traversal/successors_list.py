"""
The program creates a list of successors for a graph and performs the following operations on this graph representation:
* Breadth-first search (BFS) for traversing a graph
* Depth-first search (DFS) for traversing a graph
* Kahn's algorithm for topological sorting
* Tarjan's algorithm for topological sorting
"""
from generate_graph import *
from tabulate import tabulate


# Creates a list of edges from a given adjacency matrix
def list_of_successors(n, adjacency_matrix):
    successors = {}

    for i in range(n):
        current_successors = []
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                current_successors.append(j + 1)
        successors[i + 1] = current_successors

    return successors


def display_list_of_successors(successors):
    list_to_display = []
    for v, values in successors.items():
        row = []
        for i in values:
            row.append(" -> ")
            row.append(i)
        row.insert(0, v)
        list_to_display.append(row)

    print(tabulate(list_to_display, tablefmt="plain"))


def list_of_successors_bfs(vertices, successors):
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
                    for successor in successors[current]:
                        if visited[successor] == 0:
                            queue.append(successor)

    return bfs_order


def list_of_successors_dfs(vertices, successors):
    visited = {v: 0 for v in vertices}

    dfs_order = []

    def dfs(current):
        visited[current] = 1
        dfs_order.append(current)
        for successor in successors[current]:
            if visited[successor] == 0:
                dfs(successor)

    for v in visited:
        if visited[v] == 0:
            dfs(v)

    return dfs_order


def list_of_successors_kahns_algorithm(vertices, successors):
    in_degrees = {v: 0 for v in vertices}

    for vertex, successors_l in successors.items():
        for successor in successors_l:
            in_degrees[successor] += 1

    in_degree_0 = []
    for vertex, degree in in_degrees.items():
        if degree == 0:
            in_degree_0.append(vertex)

    result = []
    while in_degree_0:
        u = in_degree_0.pop(0)
        result.append(u)
        for successor in successors[u]:
            v = successor
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                in_degree_0.append(v)

    return result


def list_of_successors_tarjans_algorithm(vertices, successors):
    visited = {v: "white" for v in vertices}  # White - not visited

    stack = []

    def dfs(current):
        visited[current] = "gray"  # Gray - currently processing

        for successor in successors[current]:
            if visited[successor] == "white":
                dfs(successor)

        visited[current] = "black"  # Black - done
        stack.append(current)

    for v in visited:
        if visited[v] == "white":
            dfs(v)

    return stack[::-1]


num_of_vertices = int(input("Enter number of vertices: "))
adj_matrix = generate_graph(num_of_vertices)
vertices_list = [i + 1 for i in range(num_of_vertices)]

successors_list = list_of_successors(num_of_vertices, adj_matrix)
print("List of successors:")
display_list_of_successors(successors_list)

bfs = list_of_successors_bfs(vertices_list, successors_list)
print("\nBFS order:", *bfs)

dfs = list_of_successors_dfs(vertices_list, successors_list)
print("DFS order:", *dfs)

sorted_kahns = list_of_successors_kahns_algorithm(vertices_list, successors_list)
print("Topological sort using Kahn's algorithm:", *sorted_kahns)

sorted_tarjans = list_of_successors_tarjans_algorithm(vertices_list, successors_list)
print("Topological sort using Tarjan's algorithm:", *sorted_tarjans)
