class Solution:
    def climbStairs(self, n: int) -> int:
    
        # https://chatgpt.com/share/687b62ae-810c-8008-90be-419811792aa2

        memo = {}  # Cache for already-computed steps

        

        def dp(i):
            if i <= 2:
                return i  # Base cases: 1 way to climb 1 step, 2 ways for 2 steps
            if i in memo:
                return memo[i]  # Use cached result

            # Recurrence: ways(i) = ways(i-1) + ways(i-2)
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)

        # Start with Top-Down (Memoization)
        # Easier to write and understand: It’s just a recursive function + caching.
        # Natural for beginners: Feels intuitive—solve big problem by solving smaller ones.
        # Quick to prototype: You don’t have to figure out exact subproblem ordering.

        # break out the recurrence cases , either n-1 or n-2 = memo[i] = dp(i - 1) + dp(i - 2)

        # build solution recursively, using a dictionary as cache






        # n = 3
        # three ouputs (1,1,1) / (1,2) / (2,1)

        # everytime, you can only subtract by 1 or 2
        # first step in algo is to subtract a 1 or 2 then reevaluate

        # elif n > 1:   
        #     distinctWays += 1
        #     self.climbStairs(n - 1)

        #     distinctWays += 1
        #     self.climbStairs(n - 2)

        # distinctWays = 0

        # if n <= 1:
        #     return distinctWays
        
        # if n % 1 == 1:
        #     distinctWays = self.climbStairs(n-1) + self.climbStairs(n-2)

        # if n % 2 == 2:
        #     distinctWays = self.climbStairs(n-1) + self.climbStairs(n-2)

        # return distinctWays


if __name__ == "__main__":
    solution = Solution()
    # print(solution.climbStairs(2))  # Example usage, should return 2
    print(solution.climbStairs(3))  # Example usage, should return 3
    