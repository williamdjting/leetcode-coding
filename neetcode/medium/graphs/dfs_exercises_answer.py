# 1) Print numbers 1..n with recursion
def dfs_print(n: int):
    """Print numbers from 1..n using recursion."""
    if n == 0:
        return
    dfs_print(n - 1)  # go down
    print(n)          # print on the way back up


# 2) DFS traverse graph (no visited yet)
def dfs_traverse(graph: dict[str, list[str]], node: str):
    """Print nodes in DFS order (no cycle protection)."""
    print(node)
    for nei in graph.get(node, []):
        dfs_traverse(graph, nei)


# 3) DFS with visited set (cycle-safe)
def dfs_visited(graph: dict[str, list[str]], node: str, visited=None):
    """Print nodes in DFS order, no repeats (cycle-safe)."""
    if visited is None:
        visited = set()
    if node in visited:
        return
    visited.add(node)
    print(node)
    for nei in graph.get(node, []):
        dfs_visited(graph, nei, visited)


# 4) DFS count reachable nodes
def dfs_count(graph: dict[str, list[str]], start: str) -> int:
    """Return how many unique nodes are reachable from start."""
    visited = set()

    def dfs(u: str):
        if u in visited:
            return
        visited.add(u)
        for v in graph.get(u, []):
            dfs(v)

    dfs(start)
    return len(visited)


# DFS
dfs_print(3)  # 1 2 3
g = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
dfs_traverse(g, "A")  # A B D C
dfs_visited({"A":["B"],"B":["C"],"C":["A"]}, "A")  # A B C
print(dfs_count({"A":["B","C"],"B":["D"],"C":["D"],"D":[]}, "A"))  # 4