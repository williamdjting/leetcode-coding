from collections import deque

def bfs_shortest_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        node, path = queue.popleft()
        
        # Found target → return path
        if node == target:
            return path
        
        # Expand neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # no path found


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(bfs_shortest_path(graph, "A", "F"))
# Example output:
# ['A', 'C', 'F']
