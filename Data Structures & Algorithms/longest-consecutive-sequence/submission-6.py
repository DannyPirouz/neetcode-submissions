class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        i = 0
        current = 1
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i+1] == nums[i]:
                continue
            if i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        return longest
