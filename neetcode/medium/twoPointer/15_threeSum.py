class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        

        # nums = [-1,0,1,2,-1,-4]
        nums.sort() #input
        # nums = [-4, -1, -1, 0,1,2]
        threeSumList : list[list[int]] = []

        n = len(nums)

        # how three sum works is it has an anchor index, then it lets the index + 1 position and len(nums) - 1 position 
        # try to fit there values to equal the anchor, if will map through all the two pointers then move to the next anchor index
        # the anchor acts ask a guard, that is how you include a third pointer, that one only incremetns when the other two pointers are finished 
        # this way there is no duplication or weird overlaps, its very logical.

        for i in range(n):

            if i > 0 and nums [i] == nums [i - 1]:
                continue

            # this way the anchor wont duplicate its work
           
            leftPointer = i + 1
            rightPointer = n - 1
            target = -nums[i]


            while leftPointer < rightPointer: 
                s = nums[leftPointer] + nums[rightPointer]
                
                if s == target:
                    threeSumList.append([nums[leftPointer], nums[rightPointer], nums[i]])

                    # you need the below two actions in order to move the pointers forward or backward

                     # Skip duplicate lefts
                    l_val = nums[leftPointer]
                    while leftPointer < rightPointer and nums[leftPointer] == l_val:
                        leftPointer += 1

                    # Skip duplicate rights
                    r_val = nums[rightPointer]
                    while leftPointer < rightPointer and nums[rightPointer] == r_val:
                        rightPointer -= 1
            
                elif s < target:
                    leftPointer += 1 # anchor stays fixed, you check another higher value

                else:

                    rightPointer -= 1 # anchor stays fixed, you check a lower value

            #while loop keeps running until leftPointer passes the rightPointer

        return threeSumList

nums = [-1,0,1,2,-1,-4]

sol = Solution()

answer = sol.threeSum(nums)

print("answer", answer)