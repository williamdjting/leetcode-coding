from collections import deque

# ---------- BFS FUNDAMENTALS ----------

# 1) Print numbers using a queue
def bfs_print_numbers(nums: list[int]):
    """Print all numbers using a queue"""
    # TODO: put all nums in a deque
    # TODO: while queue not empty, pop left and print


# 2) BFS traverse graph
def bfs_traverse(graph: dict[str,list[str]], start: str):
    """Print BFS order"""
    # TODO: use deque
    # TODO: enqueue start
    # TODO: while queue not empty -> pop, print, enqueue neighbors


# 3) BFS with visited set
def bfs_visited(graph: dict[str,list[str]], start: str):
    """Print BFS order without revisiting"""
    visited = set([start])
    # TODO: normal BFS loop with visited check


# 4) BFS count steps from start to all nodes
def bfs_distances(graph: dict[str,list[str]], start: str) -> dict[str,int]:
    """Return shortest distance to every reachable node"""
    dist = {start: 0}
    # TODO: BFS with (node, distance)
    return dist


if __name__ == "__main__":
    bfs_print_numbers([1,2,3])  # prints 1 2 3

    g1 = {"A":["B","C"], "B":["D"], "C":[], "D":[]}
    bfs_traverse(g1, "A")   # prints A B C D
    bfs_visited({"A":["B"], "B":["C"], "C":["A"]}, "A")  # prints A B C

    g2 = {"A":["B","C"], "B":["D"], "C":["D"], "D":[]}
    print(bfs_distances(g2,"A"))
    # Expected: {'A':0, 'B':1, 'C':1, 'D':2}
