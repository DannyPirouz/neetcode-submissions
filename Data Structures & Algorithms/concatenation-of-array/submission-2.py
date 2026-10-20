class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = nums
        def dup(nums):
            for i in range(len(nums)):
                ans.append(nums[i])
            return nums
        dup(nums)
        
        return ans