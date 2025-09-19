def dfs_paths(graph, start, target):
    results = []
    
    def dfs(node, path):
        # Base case: reached target
        if node == target:
            results.append(path[:])
            return
        
        for neighbor in graph[node]:
            if neighbor not in path:  # avoid cycles
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # backtrack
    
    dfs(start, [start])
    return results


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(dfs_paths(graph, "A", "F"))
# Example output:
# [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
