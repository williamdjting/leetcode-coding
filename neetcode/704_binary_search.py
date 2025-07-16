class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # nums = [-1,0,3,5,9,12]
        # target = 9

        leftIndex = 0
        rightIndex = len(nums) - 1
        

        # for num in range(leftIndex, rightIndex):
        #     if nums[middle] == target:
        #         return num
        #     elif nums[middle] < target:
        #         leftIndex = middle + 1
        #         if leftIndex > rightIndex:
        #             return -1
        #     else:
        #         rightIndex = middle - 1

        while leftIndex <= rightIndex:

            middle = (leftIndex + rightIndex ) // 2

            # if nums[middle] == target:
            #     return middle
            # elif nums[middle] < target:
            #     leftIndex = middle + 1
            # else:
            #     rightIndex = middle - 1

            # if nums[middle] < target:
            #     leftIndex = middle + 1

            # elif nums[middle] > target:
            #     rightIndex = middle - 1
            # else:
            #     return middle

        
            if nums[middle] > target:
                rightIndex = middle - 1
        
            elif nums[middle] < target:
                leftIndex = middle + 1

            else:
                return middle

        return -1