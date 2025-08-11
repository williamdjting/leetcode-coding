class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:


        #O(n^2) brute force python 2 approach

        # double = False

        # for num1 in range(len(nums)):
        #     for num2 in range(num1+1,len(nums)):
        #         if nums[num1] == nums[num2]:
        #             double = True
        #             return True

        # return double

        
        #O(n) set approach, unique values go into a set python3 appraoch
        setList = set()


        for num1 in range(len(nums)):
            if nums[num1] in setList:
                return True
            else:
                setList.add(nums[num1])

        return False