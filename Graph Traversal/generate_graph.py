import random


# Generates directed acyclic graph for a given number (n) of vertices
def generate_graph(n):
    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    saturation = 0.5  # Number of edges was set to half of (n * (n - 1) / 2))
    num_of_edges = int(saturation * (n * (n - 1) / 2))

    edges_counter = 0

    # Directed acyclic graph is created by randomly filling the upper triangle of adjacency matrix
    while edges_counter < num_of_edges:
        i = random.randint(0, n - 2)
        j = random.randint(i + 1, n - 1)
        if adjacency_matrix[i][j] == 0:
            adjacency_matrix[i][j] = 1
            edges_counter += 1

    return adjacency_matrix
