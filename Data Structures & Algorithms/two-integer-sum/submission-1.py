class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in numbers:
                return [numbers[j], i]
            else:
                numbers[nums[i]] = i
        return []