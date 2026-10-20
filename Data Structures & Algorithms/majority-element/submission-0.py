class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurence = {}

        for num in nums:
            occurence[num] = 1 + occurence.get(num, 0)
        
        max = 0
        majorityElement = 0
        for key, value in occurence.items():
            if value > max:
                max = value
                majorityElement = key
        return majorityElement

