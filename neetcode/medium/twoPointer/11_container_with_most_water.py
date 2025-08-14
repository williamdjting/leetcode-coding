
class Solution:
    def maxArea(self, height: list[int]) -> int:
    
        # height = [1,8,6,2,5,4,8,3,7] # not used

        # 7 increments in between 8 and 7 and take the lower of the two
        # so pass an easier value to check against

        # height : list[int] = [2,5, 6, 1]

        #brute force method is O(n^2)

        n = len(height) 
        maxArea = 0
        

        for i in range(n):
            countOfIntervals = 0
            for j in range (i+1, n):
                countOfIntervals += 1
                minVal = min(height[i], height[j])
                localMaxArea = countOfIntervals * minVal
                print("height[i]", height[i], "height[j]", height[j], "minVal", minVal, "countOfIntervals", countOfIntervals, "localMaxArea", localMaxArea) #should be 49 from 8 to 7
                maxArea = max(maxArea, localMaxArea)

        print("maxArea", maxArea)
        return maxArea
    

        # to do it in O(n) implementation with two pointers solution which requires moving left and right pointers not a double for loop ever

        # you shrink the interval walls from the maximum to the minium and then you take the smallest height of the wall and find the area
        # then you take the best area calculation

        # the movement of the while left < right loop only moves depending on whether or not you want to improve the left side or right side, i.e. 
        # if the left wall is shorter it is weaker and ruining the max outcome so move to the next left pointer up to try and improve
        # if the right wall is shorter it is weaker and ruining the max outcome so move to the next right pointer down to try and improve
        # shrinking the window size of left and right based off the outcomes that are generated

        # the greedy aspect of this algo is to maximum the vertical wall size on both the left and right
        # the two pointers are used to move the list array to check and find the maxArea size with a greedy implementation that is intiated by a while left<right loop



def main():
    # height : list[int] = [2,5, 6, 1] 
    # should equal 5, because 5 is highest vertical limit * 1 interval

    height : list[int] = [1,8,6,2,5,4,8,3,7]

    sol = Solution()

    answer = sol.maxArea(height)

    # assert answer == 5, f"Expected 5 but got {answer}" # for [2,5, 6, 1]

    assert answer == 49, f"Expected 49 but got {answer}" # for [1,8,6,2,5,4,8,3,7]

if __name__ == "__main__":
    main()
