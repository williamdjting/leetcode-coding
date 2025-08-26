class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        answer : list[int] = []
        # answers[i] is equal to the product of all elements of nums except nums[i]

        
        # i have to find the product as i make a pass for the prefix (values before i)
        # i have to find the product as i make a pass for the suffix (values after i)

        for i in range(len(nums)): # goes 0,1,2,3 - stopping before 4 as length of nums is 4
            # prefix calculation
            localArr = [] 

            prefixProduct = 1
            suffixProduct = 1
            
            for l in range(0, i):
                prefixProduct *= nums[l]
            print("this is prefixProduct", prefixProduct)
            # localArr.append(prefixProduct)
            # prefixProduct = 1

            # suffix calculation
            for j in range(nums[i], len(nums)):
                suffixProduct *= nums[j]
            print("this is suffixProduct", suffixProduct)
            # localArr.append(suffixProduct)
            # suffixProduct = 1

            value = prefixProduct * suffixProduct
            answer.append(value)

        return answer


#####

sol = Solution()

nums = [1,2,3,4]

answer = sol.productExceptSelf(nums)

print("this is final answer", answer)

