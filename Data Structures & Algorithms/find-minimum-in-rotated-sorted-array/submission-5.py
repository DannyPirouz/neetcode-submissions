class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right-left) // 2

            if nums[right] > nums[middle]:
                right = middle
            else:
                left = middle + 1
        return min(nums[left], nums[right])
