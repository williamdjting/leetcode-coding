# ---------- DFS FUNDAMENTALS ----------

# 1) Print numbers 1..n with recursion
def dfs_print(n: int):
    """Print numbers from 1..n using recursion"""
    # TODO: base case: if n == 0, stop
    # TODO: recursive call on n-1
    # TODO: then print n


# 2) DFS traverse graph (no visited yet)
def dfs_traverse(graph: dict[str, list[str]], node: str):
    """Print nodes in DFS order (may revisit nodes if cycles exist)"""
    # TODO: print node
    # TODO: for each neighbor, call dfs_traverse


# 3) DFS with visited set
def dfs_visited(graph: dict[str, list[str]], node: str, visited=None):
    """Print nodes in DFS order, no repeats"""
    if visited is None:
        visited = set()
    # TODO: if already visited, return
    # TODO: mark visited
    # TODO: print node
    # TODO: recurse neighbors


# 4) DFS count reachable nodes
def dfs_count(graph: dict[str, list[str]], start: str) -> int:
    """Return how many unique nodes are reachable from start"""
    visited = set()
    # TODO: write inner dfs that fills visited
    # TODO: run dfs(start)
    return len(visited)


if __name__ == "__main__":
    # Expected
    dfs_print(3)  # prints 1 2 3

    g1 = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
    dfs_traverse(g1, "A")  # e.g. prints A B D C

    g2 = {"A":["B"], "B":["C"], "C":["A"]}
    dfs_visited(g2, "A")  # prints A B C

    g3 = {"A":["B","C"], "B":["D"], "C":["D"], "D":[]}
    print(dfs_count(g3, "A"))  # 4
