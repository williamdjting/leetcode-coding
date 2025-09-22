from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #1) build adjacency list
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for u, v in prerequisites:
            graph[v].append(u) #v-> u (b depends on a), different from 207
        #2) 
        visited = [0] * numCourses

        #5) order list
        order : list[int] = []

        #4) build dfs
        def dfs(node: int) -> bool:
            if visited[node] == 1:
                return False
            
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
                
            visited[node] = 2
#            order.append(visited[node]) # this pushes the contents of [node], should push node itself
            order.append(node)

            return True

        #3)
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        
        order.reverse()
        return order
    


sol = Solution()

numCourses = 4

prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# Output: [0,2,1,3]

answer = sol.findOrder(numCourses, prerequisites)

print("answer", answer)