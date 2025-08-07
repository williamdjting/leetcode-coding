class Solution:
    def singleNumber(self, nums: list[int]) -> int:


        hashMap = {}

            # for num in nums:
            #     if num not in hashMap:
            #         hashMap[nums[num]] = 1
            #     elif num in hashMap:
            #         hashMap[nums[num]] += 1

            
            # for nums[num], count in hashMap.items():
            #     if count == 1:
            #         print("value", nums[num])

                
        #     # Count occurrences
        # for num in nums:
        #     if num not in hashMap:
        #         hashMap[num] = 1
        #     else:
        #         hashMap[num] += 1

        # # Find the number with count 1
        # for num, count in hashMap.items():
        #     if count == 1:
        #         print(num)
        #         return num  # or print(num)



        result = 0
        for num in nums:
            result ^= num
        print(result)




nums = [4,1,2,1,2]

sol = Solution()

sol.singleNumber(nums)
