class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = nums[0]

        for num in nums:
            if currSum >= 0 and num >= 0:
                currSum += num
                res = max(res, currSum)
            elif currSum >= 0 and num < 0:
                currSum += num
                res = max(res, currSum)
            elif currSum < 0 and num >= 0:
                currSum = num
                res = max(res, currSum)
            elif currSum < 0 and num <= 0:
                currSum = num
                res = max(res, currSum)
            
        return res
