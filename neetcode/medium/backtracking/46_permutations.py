from typing import List

# actual solution https://chatgpt.com/share/68e75926-f00c-8008-b7b1-18e0dca00c6d

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        path: List[int] = []
        used = [False] * len(nums)   # track which elements are already in the path

        def dfs():
            # base case: all numbers are used → one complete permutation
            if len(path) == len(nums):
                res.append(path[:])  # append a *copy* of path
                return

            for i in range(len(nums)):
                if used[i]:          # skip if already used
                    continue
                used[i] = True       # choose nums[i]
                path.append(nums[i]) # add to current permutation
                dfs()                # explore further
                path.pop()           # backtrack (remove last element)
                used[i] = False      # un-choose (mark as unused again)

        dfs()
        return res

# test
sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))



# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # Given an array nums of distinct integers, return all the possible permutations. A permutation is a rearrangement of all the elements in the array. You can return the answer in any order
        
        
#         nums.sort()
#         res: List[List[int]] = []
        
        
#         def dfs(indexPosition : int, nums : List[int], path : List[int]) -> None:
            
#             if nums is None:
#                 return None
            
#             if len(nums) <= 0:
#                 return None
            
#             if indexPosition == len(nums):
#                 res.append(path.copy())
#                 return
            
#             for i in range(indexPosition, len(nums)):
#                 value = nums[i]

#                 path.append(value)
#                 dfs(i+1, nums, path)
#                 path.pop()
        
        
#         dfs(0, nums, [])
        
#         return res
        
        
        
sol = Solution()

nums = [1,2,3]

output = sol.permute(nums)

print("output", output)

#output [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


