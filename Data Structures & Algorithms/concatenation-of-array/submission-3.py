class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = []
        def dup(nums):
            for i in range(len(nums)):
                ans.append(nums[i])
            return nums
        for _ in range(2):
            dup(nums)
        
        return ans