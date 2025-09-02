class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # initial idea:  
        # total number of subarrays that sum equals to k
        # subarrays can be any size so long as they sum to k and are less than or equal to length of nums array
        # first pass of all the numbers in nums list then store each instance of a number in a hash map with count frequency
        # given k, minus values from k based off the number of hashmap letters and their frequencies
        # brute force every combination but start from the largest value first, how many subarrays can be made from the biggest value, then the next, etc...
        # sorted_nums = sorted(nums, reverse=True) this is the biggest value first

        # store the subarray == k as a list, convert it into a tuple, then create a hashmap of all combinations of tuples 
        # that sum to k and then check for duplicates
        # count the hashmap to find the total number of subarrays whose sum equals to k

        # my answer
        # sortedNums = sorted(nums, reverse=True)

        # res: list[tuple[int, ...]] = []

        # tempList = []
        # tempVal = k
        # # j = i
        # seen: set[tuple[int, ...]] = set()
        # count = 0

        # for i in range(len(sortedNums)):
        #     j = i
        #     if tempVal - sortedNums[i] < 0:
        #         break

        #     if tempVal - sortedNums[i] == 0:
        #         res.append(tuple(sortedNums[i]))

        #     while tempVal >= 0:
        #         if tempVal - sortedNums[j] < 0:
        #             break   
        #         if tempVal == 0:
        #             res.append(tuple(tempList))
        #             break
        #         tempVal = tempVal - sortedNums[j]
        #         tempList.append(sortedNums[j])
        #         j += 1

        # # this will store all the subarrays as tuples in res

        # for tuple in res:
        #     if tuple not in seen:
        #         seen.add(tuple)
        #         count += 1

        #     if tuple in seen:
        #         break

        # return count

        # Keep your idea of gathering found subarrays as tuples in `res`
        # and scanning with i (start) and j (extend forward).
        res: list[tuple[int, ...]] = []
        count = 0

        # Do NOT sort: subarrays must remain contiguous in the original order. KEY POINT
        n = len(nums)

        for i in range(n):
            temp_sum = 0
            temp_list: list[int] = []

            # extend the window [i..j]
            for j in range(i, n):
                temp_sum += nums[j]
                temp_list.append(nums[j])

                if temp_sum == k:
                    # store the subarray as a tuple (like you intended)
                    res.append(tuple(temp_list))
                    count += 1
                # optional micro-optimization if all numbers were non-negative:
                # if temp_sum > k: break
                # but we can't assume that for general inputs

        # If you wanted to deduplicate identical VALUE-patterns, you could use a set,
        # but for the standard "subarray sum equals k" problem, each occurrence counts.
        # seen = set(res); unique_count = len(seen)

        return count


nums = [ 1,2,3]

k = 2

sol = Solution()

answer = sol.subarraySum(nums, k)

print("this is answer", answer)