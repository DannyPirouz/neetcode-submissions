class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def houseRob(houses):
            memo = [-1] * (len(houses) + 1)

            def dp(i):
                if i < 0:
                    return 0
                if i == 0:
                    return houses[0]
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(dp(i-2) + houses[i], dp(i-1))
                return memo[i]
            return dp(len(houses) - 1)

        value1 = houseRob(nums[:-1])
        value2 = houseRob(nums[1:])

        return max(value1, value2)

