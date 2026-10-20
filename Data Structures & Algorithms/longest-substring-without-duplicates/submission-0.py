class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        output = 0
        left = 0

        for right in range(len(s)):
            if s[right] in charSet:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
            charSet.add(s[right])
            output = max(output, right - left + 1)
                
        return output

