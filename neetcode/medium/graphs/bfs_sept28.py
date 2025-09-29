from collections import deque, defaultdict
from typing import Dict, List, Tuple, DefaultDict, Deque, Set


class Solution:
    def graph(self, edges: List[Tuple[int, int]]) -> DefaultDict[int, List[int]]:
        g: DefaultDict[int, List[int]] = defaultdict(list)
        for u, v in edges:
            if v not in g[u]:
                g[u].append(v)
            if u not in g[v]:  # add reverse edge
                g[v].append(u)
        return g

    def bfs(self, graph: DefaultDict[int, List[int]], start: int) -> List[int]:
        if start not in graph:
            return []

        visited: Set[int] = {start}
        order: List[int] = []
        queue: Deque[int] = deque([start])

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return order


sol = Solution()

edges = [(1, 2), (1, 3), (2, 4), (3, 4)]

graph = sol.graph(edges)
order = sol.bfs(graph, 3)

print("Adjacency:", dict(graph))
print("BFS from 3:", order)

# Assertions
assert order[0] == 3
assert set(order) == {1, 2, 3, 4}