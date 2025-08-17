import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()

        # [1,2,3,4,5,6]
        # nums [ 6 -2 ] = nums[4] = 5
        # return nums[len(nums) - k]


        # # find the largest k element , use min heap
        return heapq.nlargest(k, nums)[-1]
    
        # find the smallest k element , use max heap
        # return heapq.nsmallest(k, nums)[-1]

# nums = [3,2,1,5,6,4], k = 2

nums = [3,2,3,1,2,4,5,5,6]
k = 4

sol = Solution()



answer = sol.findKthLargest(nums, k)

print(answer)