"""
The program creates an adjacency matrix for a graph and performs the following operations on this graph representation:
* finding an Eulerian cycle using Depth First Search (DFS)
* finding a Hamiltonian cycle using the Roberts-Flores algorithm
"""
import random
import copy


# Generates a connected undirected graph with n vertices and given graph saturation s
def graph_generation(n, s):
    graph = [[0] * n for _ in range(n)]
    num_of_edges = (n * (n - 1)) // 2 * s
    vertices = list(range(n))
    random.shuffle(vertices)

    curr_num_of_edges = 0

    for i in range(n - 1):
        graph[i][i + 1] = 1
        graph[i + 1][i] = 1
        curr_num_of_edges += 1

    graph[0][n - 1] = 1
    graph[n - 1][0] = 1
    curr_num_of_edges += 1

    while curr_num_of_edges < num_of_edges - 3:
        v1 = random.randint(0, n - 1)
        v2 = random.randint(0, n - 1)
        v3 = random.randint(0, n - 1)
        if graph[v1][v2] == 0 and graph[v1][v3] == 0 and graph[v3][v2] == 0 and v1 != v2 and v1 != v3:
            graph[v1][v2] = graph[v2][v1] = graph[v1][v3] = graph[v3][v1] = graph[v2][v3] = graph[v3][v2] = 1
            curr_num_of_edges += 3
    print(graph)
    return graph


def dfs_euler(v, adjacency_matrix_copy, stack):
    for u in range(len(adjacency_matrix_copy)):
        if adjacency_matrix_copy[v][u] > 0:
            adjacency_matrix_copy[v][u] -= 1
            adjacency_matrix_copy[u][v] -= 1
            dfs_euler(u, adjacency_matrix_copy, stack)

    stack.append(v)


def eulerian_cycle(adjacency_matrix):
    stack = []
    adjacency_matrix_copy = copy.deepcopy(adjacency_matrix)

    dfs_euler(0, adjacency_matrix_copy, stack)

    return stack


def hamiltonian_helper(n, adjacency_matrix, cycle, v):
    if v == n:
        if adjacency_matrix[cycle[v - 1]][cycle[0]] == 1:
            cycle.append(cycle[0])  # closing cycle
            return True
        else:
            return False

    for v in range(1, len(adjacency_matrix)):
        if adjacency_matrix[cycle[v - 1]][v] == 1 and v not in cycle:
            cycle[v] = v

            if hamiltonian_helper(n, adjacency_matrix, cycle, v + 1):
                return True

            cycle[v] = -1

    return False


def hamiltonian_cycle(n, adjacency_matrix):
    cycle = [-1] * n
    cycle[0] = 0

    if not hamiltonian_helper(n, adjacency_matrix, cycle, 1):
        return False

    return cycle


num_of_nodes = int(input("Enter the number of the graph nodes: "))
saturation = 0.7  # saturation of the edges
adj_matrix = graph_generation(num_of_nodes, saturation)

print("Eulerian cycle:", eulerian_cycle(adj_matrix))
print("Hamiltonian cycle:", hamiltonian_cycle(num_of_nodes, adj_matrix))
