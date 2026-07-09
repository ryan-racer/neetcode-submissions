class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = prices[0]

        for p in prices:
            j = min(j, p)
            i = max(i, p-j)
        
        return i
