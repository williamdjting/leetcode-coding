#1. two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # check the number in the range from 0 to the length of the nums list

        # check the number + 1 in the range (start at i + 1, and end at length of nums list)

        # if the number at index i == number at index j == target

 #           return the value of the two (i,j)


        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j]) == target:
                    return (i, j)