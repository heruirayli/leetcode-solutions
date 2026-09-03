class Solution(object):
    """
    :type prices: List[int]
    :rtype: int
    """
    # time    O(n^2)
    # space   O(1)
    def maxProfit_v1(self, prices):
      maxProfit = 0
      for buy in range(len(prices)-1):
        for sell in range(i,len(prices)):
          diff = prices[sell] - prices[buy]
          if diff > maxProfit:
            maxProfit = diff
      return maxProfit

    # time    O(n)
    # space   O(1)
    def maxProfit_v2(self, prices):
      maxProfit = 0
      minPrice = prices[0]
      for sell in range(1,len(prices)):
        currentPrice = prices[sell]
        if minPrice > currentPrice:
          minPrice = currentPrice
        else:
          diff = currentPrice - minPrice
          if diff > maxProfit:
            maxProfit = diff
      return maxProfit

output = Solution()
print(output.maxProfit_v2([7,1,5,3,6,4]))