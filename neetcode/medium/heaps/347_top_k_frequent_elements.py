# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # sorting answer - this answer puts the sorted value into an array list then pops this arr's first value 
        # the head which is the largest value after sorting and appends it into the results array 
        # this implementation i believe works for [-1] output
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        # steps to solve
        # create a hashmap that counts the occurence of a number in the nums list
        # take only the top k amount of numbers in the list that have the highest counts


        # my implementation, generally works except for the [-1] because it doesnt use a pop of another array into a result list
        count = {}


        for num in nums:
            if num not in count:
                count[num] = 0 #initialize to avoid key error
            count[num] += 1

        # alternative is get
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # hashmap creation is finished

        # fetch the top k amount of numbers from count hashmap
        # first find the first highest number

        
        returnList = [None] * k # list of size k to be filled

        sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for i in range(len(returnList)):

            # for number, countOfNumber in sorted_counts:
            #     returnList[number] = number # this needs to iterate forward

            #     break
            number, countOfNumber = sorted_counts[i]
            returnList[i] = number

        return returnList
            

sol = Solution()

nums = [1,1,1,2,2,3]

k = 2

answer : list[int] = sol.topKFrequent(nums, k)

print("this is answer", answer)