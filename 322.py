class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[0]+[float('inf')] * amount

        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i],dp[i-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
