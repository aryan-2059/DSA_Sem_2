graph = {}
def add_edge(u, v, w):
    if u not in graph: graph[u] = []
    graph[u].append((v, w))

add_edge('A', 'B', 5); add_edge('B', 'C', 3)

visited = set()
def dfs(graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(graph, neighbor[0])

dfs(graph, 'A')