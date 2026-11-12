class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        left = 0
        
        for right in range(len(s)):
            length = (right+1) - left
            count[s[right]] += 1 
            maxFreq = max(count.values())

            if (length - maxFreq) <= k:
                res = max(res, length)
            else:
                count[s[left]] -= 1
                left += 1
        return res



        