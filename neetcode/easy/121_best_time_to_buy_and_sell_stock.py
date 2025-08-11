class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # prices = [ 7,1,5,3,6,4]
        # brute force
        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = prices[j] - prices[i]
        #         if maxProfit > profit:
        #             profit = prices[j] - prices[i]

        
        # return profit


        #in checking each price,
        # we are either setting the new price lower (floor),
        # or we are setting the new max profit (ceiling)


        #prices = [10,1,5,6,7,1]

        minPrice = float('inf') # starts at 1000
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price # find the floor
            else:
                profit = price - minPrice # find the current floor to current price, profit
                maxProfit = max(maxProfit, profit) # is this profit the highest possible

        return maxProfit # return max found