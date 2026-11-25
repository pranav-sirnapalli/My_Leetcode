class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        dp = [[0] * 2 for i in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            buy = -prices[i] + dp[i-1][0]
            skip = dp[i-1][1]
            dp[i][1] = max(buy, skip)

            sell = prices[i] + dp[i-1][1] - fee
            hold = dp[i-1][0]
            dp[i][0] = max(sell, hold)
        return dp[-1][0]