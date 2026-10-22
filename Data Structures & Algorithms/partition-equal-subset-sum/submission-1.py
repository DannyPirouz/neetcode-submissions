class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        memo = [[-1] * (target + 1) for _ in range(len(nums))]

        def dp(i, remaining):
            if remaining == 0:
                return True
            if i >= len(nums) or remaining < 0:
                return False
            if memo[i][remaining] != -1:
                return memo[i][remaining]
            memo[i][remaining] = dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)
            return memo[i][remaining]
        return dp(0, target)