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

        minPrice = float('inf')

        maxProfit = 0

        #in checking each price,
        # we are either setting the new price lower (floor),
        # or we are setting the new max profit (ceiling)


        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                maxProfit = max(maxProfit, profit)

        return maxProfit