from collections import deque

# 1) Print numbers using a queue
def bfs_print_numbers(nums: list[int]):
    """Print all numbers using a queue (FIFO)."""
    q = deque(nums)
    while q:
        print(q.popleft())


# 2) BFS traverse graph (no cycles assumed here)
def bfs_traverse(graph: dict[str, list[str]], start: str):
    """Print BFS order (level-by-level)."""
    q = deque([start])
    while q:
        node = q.popleft()
        print(node)
        for nei in graph.get(node, []):
            q.append(nei)


# 3) BFS with visited set (cycle-safe)
def bfs_visited(graph: dict[str, list[str]], start: str):
    """Print BFS order without revisiting nodes."""
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        print(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)


# 4) BFS distances (shortest steps from start to all)
def bfs_distances(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    """Return shortest distance (edge count) to every reachable node."""
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in graph.get(node, []):
            if nei not in dist:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist




# BFS
bfs_print_numbers([1,2,3])  # 1 2 3
bfs_traverse(g, "A")        # A B C D
bfs_visited({"A":["B"],"B":["C"],"C":["A"]}, "A")  # A B C
print(bfs_distances({"A":["B","C"],"B":["D"],"C":["D"],"D":[]}, "A"))  # {'A':0,'B':1,'C':1,'D':2}
