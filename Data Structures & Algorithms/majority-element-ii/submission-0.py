class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3

        occurence = {}
        result = []

        for num in nums:
            occurence[num] = 1 + occurence.get(num, 0)
        
        for key, value in occurence.items():
            if value > threshold:
                result.append(key)

        return result
