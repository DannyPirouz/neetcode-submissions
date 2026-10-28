class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        current = 0
        longest = 0
        for s in seen:
            if s-1 not in seen:
                current += 1
                while True:
                    if s+1 in seen:
                        current += 1
                        s = s+1
                        continue
                    break
                longest = max(longest, current)
                current = 0
        return longest
