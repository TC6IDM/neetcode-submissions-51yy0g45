class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 9999999999999999999999
        profit = 0

        for i in range(len(prices)):

            if prices[i]<l: l = prices[i]

            if prices[i]-l > profit: profit =  prices[i]-l
        
        return profit

        