from typing import List

class Solution:
    # steps to solve,
    # 1) build the adjacency list using hashmap
    # 2) build the visiting status for each node
    # 3) build the search loop to call dfs based off visiting status
    # 4) build the dfs that marks the visiting status of i index (which is same index for visited and graph)
    # 4) the dfs will mark if its 1 or 2, and then explore on each neighbour of the graph (via adj list) to find if 
    # its neighbours have cycles, return False at any point if back edge, else returns True bubbles to top

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for u, v in prerequisites:
            graph[u].append(v)

        visited = [0] * numCourses # to be filled with statuses , 0, 1, 2

        def dfs(node: int) -> bool:
            if visited[node] == 1: 
                # node is in recursion stack → cycle
                # if you come back to visited[node] in your dfs exploration, return false as their is a backedge neighbour
                return False
            if visited[node] == 2:
                # node already fully explored
                return True

            visited[node] = 1 # first encounter of visited[node] , mark as visiting

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            visited[node] = 2 # finished visiting safe

            return True # done this dfs and its recursions

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False                
        return True




sol = Solution()

numCourses = 2

prerequisites = [[1,0],[0,1]]

answer = sol.canFinish(numCourses, prerequisites)

print("answer", answer)

'''
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, 
and to take course 0 you should also have finished course 1. 
So it is impossible.

If you have a cyclical graph then you cannot fulfill this, 
If G is a DAG, then G has a topological ordering. 
Must have topological ordering (no cycle) to be True.
'''