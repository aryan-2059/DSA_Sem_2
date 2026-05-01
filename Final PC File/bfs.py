graph = {}
def add_edge(u, v, w):
    if u not in graph: graph[u] = []
    graph[u].append((v, w))

add_edge('A', 'B', 5); add_edge('B', 'C', 3)

def bfs(graph, start):
    visited = [start]
    queue = [start]
    while queue:
        u = queue.pop(0)
        print(u, end=" ")
        for v in graph.get(u, []):
            if v[0] not in visited:
                visited.append(v[0])
                queue.append(v[0])

bfs(graph, 'A')