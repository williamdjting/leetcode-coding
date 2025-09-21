from __future__ import annotations
from typing import Optional, Dict, List
from collections import deque

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List[Node]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None

        old_to_new: Dict[Node, Node] = {}

        def dfs(cur: Node) -> Node:
            if cur in old_to_new:
                return old_to_new[cur]
            copy = Node(cur.val)
            old_to_new[cur] = copy
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)



# my attempt

# # Definition for a Node.
# class Node:
#     def __init__(self, val : int, neighbors : int):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []


# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
#         if node[0] == [] or node is None:
#             return None

#         newAdjList : list[list[int]] = [[] for _ in range(len(adjList))]

        
#         for index, neighbors in enumerate(adjList, start=0):
#             #build by appending each neighbour
#             # newAdjList.append(neighbors)

#             #build a pre-sized newAdjList
#             newAdjList[index].extend(neighbors)

#         return newAdjList
# n3 = Node(3)
# n2 = Node(2, n3)
# n1 = Node(1, n2)


adjList : list[list[int]] = [[2,4],[1,3],[2,4],[1,3]]

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]

# adjList[0] = [2,4]
# adjList[1] = [1,3]
# adjList[2] = [2,4]
# adjList[3] = [1,3]

sol = Solution()

answer = sol.cloneGraph(adjList)

print("answer", answer)

# print(sol.cloneGraph(n1).val)
# print(sol.cloneGraph(n2).val)
# print(sol.cloneGraph(n3).val)

