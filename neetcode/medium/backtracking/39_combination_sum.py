from typing import List

class Solution:
    # my solution

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
    #     candidates.sort() # to handle duplicates 
    #     result : List[List[int]] = []
    #     lengthOfCandidate = len(candidates)
        
        
    #     def search(target, path):
    #         # only append when target = 0
    #         # if path[:] not in result:            
    #         #     result.append(path[:])
    #         for i in range(lengthOfCandidate):
    #             path.append(candidates[i])
    #             newTarget = target - candidates[i]
    #             if newTarget <= 0:
                    
    #                 path.pop()
    #                 continue
    #             search(newTarget, path)
    #             path.pop()
                
    #     search(target, [])
    #     return result

    # solution is https://chatgpt.com/share/68e609e3-1ad8-8008-83ab-67fd8b43eab6
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Optional: sort to help with small pruning and duplicate handling if input has duplicates
        candidates.sort()
        res: List[List[int]] = []

        def dfs(start: int, remain: int, path: List[int]) -> None:
            # Base cases
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0:
                return  # prune

            # Try each candidate at or after 'start'
            for i in range(start, len(candidates)):
                c = candidates[i]

                # Optional: skip duplicate candidate values at the same depth (protects against duplicate inputs)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(c)
                # Allow reuse of the same candidate -> pass i (not i+1)
                dfs(i, remain - c, path)
                path.pop()  # one pop for one append

        dfs(0, target, [])
        return res

sol = Solution()

candidates = [2,3,6,7]

target = 7

# output should be [[2,2,3],[7]]

answer = sol.combinationSum(candidates, target)

print("answer", answer)