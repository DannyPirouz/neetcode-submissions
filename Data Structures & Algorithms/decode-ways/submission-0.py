class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)

        def dp(i):
            if i == 0:
                return 1
            if memo[i] != -1:
                return memo[i]
            total = 0
            if s[i-1] != "0":
                total += dp(i-1)
            if i-2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
                total += dp(i-2)
            memo[i] = total
            return memo[i]
        return dp(len(s))
