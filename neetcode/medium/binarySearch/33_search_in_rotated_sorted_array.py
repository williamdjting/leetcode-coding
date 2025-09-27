

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left , right = 0 , len(nums) - 1


        while left <= right :

            middle = (left + right) // 2 # middle index is 3 in this case

            if nums[middle] == target: # nums[middle] = 7 target is 0 in this case
                return middle

            # my solution
            # elif nums[middle] > target: # 7 > 0
            #     # search for target , this means 


            #     if nums[middle] > nums[left]: #indicates ascending order before a pivot
            #     # nums[left] = 4, nums[middle] = 7
            #     # shift left to be right of the middle
            #         left = middle + 1
            #         # left is now index 4 so on next run it will be < middle
            #     if nums[left] == target:
            #         return left
                

            # else: # nums[middle] < target # 0 < target is 8 or more
                
            #     if nums[middle] < nums[right]:
            #         #that means nums[middle] 7 < nums[right] which is >7 which means ascending order
            #         right = middle - 1
            #     if nums[right] == target:
            #         return right

            # Determine which half is sorted
            if nums[left] <= nums[middle]:
                # Left half [l..m] is sorted
                if nums[left] <= target < nums[middle]:
                    right = middle - 1  # target is in the left half
                else:
                    left = middle + 1  # target is in the right half
            else:
                # Right half [m..r] is sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1  # target is in the right half
                else:
                    right = middle - 1  # target is in the left half


        return -1




nums = [4,5,6,7,0,1,2]
target = 3

sol = Solution()

answer = sol.search(nums, target)

print("this is answer", answer)