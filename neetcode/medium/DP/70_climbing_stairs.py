# https://leetcode.com/problems/climbing-stairs/description/

from typing import List
from collections import defaultdict

# incorrect, makes many instances of numberOfDistinctWays
# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         numberOfDistinctWays = defaultdict(int)
        
#         # if n <= 1:
#         #     return n
        
#         if n <= 2:
#             return n
        
#         numberOfDistinctWays[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
#         return numberOfDistinctWays[n]

class Solution:
    def __init__(self):
        self.numberOfDistinctWays = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.numberOfDistinctWays:
            return self.numberOfDistinctWays[n]
        
        self.numberOfDistinctWays[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.numberOfDistinctWays[n]



sol = Solution()

answer = sol.climbStairs(3)
        
print("this is answer", answer)

# assert(answer == 2), True

