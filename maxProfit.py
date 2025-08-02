def maxProfit(prices):
  max_p = 0
  min_p = float('inf')
  for i in range(0,len(prices)):
    min_p = min(min_p,prices[i])
    profit = prices[i] - min_p
    max_p = max(max_p,profit)
  return max_p
print(maxProfit(prices))
