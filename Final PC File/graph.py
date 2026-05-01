graph = {}
def add_edge(u, v, w):
    if u not in graph: graph[u] = []
    graph[u].append((v, w))

add_edge('A', 'B', 5); add_edge('B', 'C', 3)
print(graph)