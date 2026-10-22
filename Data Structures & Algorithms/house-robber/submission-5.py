class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)

        def dp(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[i]
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dp(i-2) + nums[i], dp(i-1))
            return memo[i]
        return dp(len(nums) - 1)
            