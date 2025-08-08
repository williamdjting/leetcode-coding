# cool question , my favourite so far

# class Solution:
#     def isHappy(self, n: int) -> bool:


#         digits = []

#         while n > 0:
#             digits.append(n % 10) # take last digit
#             n //= 10 # remove last digit

#         # loops until it ends


#         squaredDigits = list(map(lambda x: x ** 2, digits))

#         total = sum(squaredDigits)

#         print(total) # 1

#         if total == 1:
#             return True
        
#         else:
#             return self.isHappy(total)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To avoid infinite loops by detecting cycles
        
        while n != 1 and n not in seen:
            seen.add(n)
            digits = [int(d) for d in str(n)]  # more straightforward digit extraction
            squaredDigits = list(map(lambda x: x ** 2, digits))
            n = sum(squaredDigits)
        
        return n == 1


sol = Solution()

returnVal = sol.isHappy(19)

print(returnVal)