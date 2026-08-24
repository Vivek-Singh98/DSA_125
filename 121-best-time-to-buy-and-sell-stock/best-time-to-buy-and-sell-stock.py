class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        left = 0
        right =1
        while(right<len(prices)):
            if prices[left]<prices[right]:
                profit = prices[right] - prices[left]
                if(max<profit):
                    max=profit
            else:
                left=right
            right=right+1

        return max                
