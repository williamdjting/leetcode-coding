class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # my implementation works, should be multiple prefix and suffix and reset to 1, no need for localArr

        # answer : list[int] = []
        # # answers[i] is equal to the product of all elements of nums except nums[i]

        
        # # i have to find the product as i make a pass for the prefix (values before i)
        # # i have to find the product as i make a pass for the suffix (values after i)

        # for i in range(len(nums)): # goes 0,1,2,3 - stopping before 4 as length of nums is 4
        #     # prefix calculation
        #     localArr = [] 

        #     prefixProduct = 1
        #     suffixProduct = 1

        #     for l in range(0, i):
        #         prefixProduct *= nums[l]
        #     print("this is prefixProduct", prefixProduct)
        #     # localArr.append(prefixProduct)
        #     # prefixProduct = 1

        #     # suffix calculation
        #     for j in range(nums[i], len(nums)):
        #         suffixProduct *= nums[j]
        #     print("this is suffixProduct", suffixProduct)
        #     # localArr.append(suffixProduct)
        #     # suffixProduct = 1

        #     value = prefixProduct * suffixProduct
        #     answer.append(value)

        # return answer

        # chatgpt implementation
        # it gives the product of the left side up to i (but not including) 
        # multiplied by the product of the right side up to i (but not including)

        n = len(nums)
        answer = [1] * n

        # prefix products into answer
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
    
        # this sums up the value of answer by prefix first then suffix first for each index position
        # prefix *= nums[i] → builds up the product of everything before the current index.
        # suffix *= nums[i] → builds up the product of everything after the current index.
        # answer[i] stores the left product from pass 1, then gets multiplied by the right product in pass 2.


#####

sol = Solution()

nums = [1,2,3,4]

answer = sol.productExceptSelf(nums)

print("this is final answer", answer)

