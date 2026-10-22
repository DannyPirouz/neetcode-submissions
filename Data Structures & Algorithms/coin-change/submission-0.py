class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)

        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return float('inf')
            if memo[i] != -1:
                return memo[i]
            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, 1 + dp(i - coin))
            memo[i] = minCoins
            return memo[i]
        res = dp(amount)
        if res == float('inf'):
            return -1
        return res

            