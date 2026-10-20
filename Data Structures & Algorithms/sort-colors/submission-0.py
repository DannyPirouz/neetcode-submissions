class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        orderedNums = []
        for num in nums:
            if num == 0:
                orderedNums.append(num)
        for num in nums:
            if num == 1:
                orderedNums.append(num)
        for num in nums:
            if num == 2:
                orderedNums.append(num)
        nums[:] = orderedNums