import math

class Solution:
    def findMin(self, nums: list[int]) -> int:

        # write the algo for rotation of the array 1 to n times, each time is just a shift forward

        # this is O(n)
        # n = 3
        # # rotation of each index 3 times becomes [3,4,5,1,2]
        # def shift_array_in_place(nums: list[int], n: int) -> list[int]:
        #     n = n % len(nums)
        #     for num in range(n):
        #         last = nums.pop()
        #         nums.insert(0, last)
        #     return nums
        

        # rotatedNums : list[int] = shift_array_in_place(nums, n)
        # print("rotatedNums", rotatedNums)

        # # return rotatedNums # returns [3,4,5,1,2]

        # rotatedNums.sort()

        # sortedRotatedNums : list[int] = rotatedNums

        # print ("sortedRotatedNums", sortedRotatedNums)

        # answer = sortedRotatedNums[0]

        # return answer


        # to do in O(log n ) must use binary search

        
         # this is the middle index , 2 in this context
        left = 0 # this is left index
        right = len(nums) - 1 # this is right index

        res = nums[0]

        while left <= right:

            if nums[left] < nums[right]: # if its sorted its an classic binary search array case so you can just pick the most left value as that is the smallest
                res = min (res, nums[left])
                break

            middle = math.floor( (left + right) / 2) # if its not sorted, then I have to find the middle index value, then compare it
            res = min (res, nums[middle])

            if nums[middle] >= nums[left]: # so the middle index value is larger so the 
                left = middle + 1

            else: 
                right = middle - 1

        return res

nums : list [int] = [3,4,5,1,2]

sol = Solution()

answer = sol.findMin( nums )

print("this is the answer", answer)
# should be 1



