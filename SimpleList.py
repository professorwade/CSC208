# Example graph with 4 vertices
adjacency_list = {
    0: [1, 2],   # Vertex 0 is connected to vertices 1 and 2
    1: [0, 2, 3], # Vertex 1 is connected to vertices 0, 2, and 3
    2: [0, 1, 3], # Vertex 2 is connected to vertices 0, 1, and 3
    3: [1, 2]    # Vertex 3 is connected to vertices 1 and 2
}

# Print adjacency list
for vertex, neighbors in adjacency_list.items():
    print(f"{vertex}: {neighbors}")
