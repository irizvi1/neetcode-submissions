class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        currprofit  = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                currprofit = prices[j] - prices[i]
                maxprofit = max(maxprofit, currprofit)
        if maxprofit <= 0:
            return 0
        else:
            return maxprofit