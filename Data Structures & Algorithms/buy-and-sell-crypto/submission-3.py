class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #set l to index 0, r to index 1 and if l > r, increment l and r
        #
        
        l, r = 0, 1
        maxprofit = 0
        curprofit = 0

        while r < len(prices):
            while prices[r] < prices[l] and r < len(prices) -1 :
                l = r
                r+=1
            curprofit = prices[r] - prices[l]
            maxprofit = max(maxprofit, curprofit)
            r+=1
        if maxprofit <= 0:
            return 0
        else:
            return maxprofit
            
