class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        
        # if nums is None:
        #     return 0


        # nums.sort() #sort from lowest to highest

        # print("nums", nums)

        # # nums = [1, 2, 3, 4, 100, 200]
        # count = 0

        # left = 0
        # right = left + 1

        # lengthOfNums = len(nums)

        # count = 1


        # while right <= lengthOfNums - 1: # 0 1 1 2
        #     print("nums[left]", nums[left])
        #     print("nums[right]", nums[right])

        #     if nums[left] < 0 or nums[right] < 0:
        #         count += 0

        #     if nums[left] == nums[right] - 1 : # 1 == 1
        #         print("1", nums[left], ",", nums[right] + 1)
        #         count += 1

        #     elif nums[left] == nums[right]:
        #         count += 0    
        #         print("2", nums[left], ",", nums[right] + 1)

        #     left += 1
        #     right += 1
            
            
        # return count

        # Handle None/empty first
        if not nums:
            return 0

        nums.sort()  # ascending

        best = 1
        curr = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                # skip duplicates
                continue
            if nums[i] == nums[i + 1] - 1:   # preferred (ascending check)
                curr += 1
            # If you really want the reversed form:
            # if nums[i] == nums[i + 1] + 1: 
            #     curr += 1
            else:
                best = max(best, curr)
                curr = 1

        return max(best, curr)




sol = Solution()

nums = [0,3,7,2,5,8,4,6,0,1]

answer = sol.longestConsecutive(nums)

print("this is answer (an int)", answer)
