class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_min, p_max = 0, 0
        profit = 0

        while p_max <= len(prices) - 1:
            if prices[p_min] == prices[p_max]:
                p_max += 1
            elif prices[p_min] > prices[p_max]:
                p_min += 1
            else:
                profit = max(profit, prices[p_max] - prices[p_min])
                p_max +=1
        return profit
                



"""
[10,1,5,6,7,1]

[10,1,5,6,7,1]
"""