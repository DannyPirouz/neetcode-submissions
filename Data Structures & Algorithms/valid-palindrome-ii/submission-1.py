class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                first = self.validPal(s, left, right - 1)
                second = self.validPal(s, left + 1, right)
                if first or second:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True

    def validPal(self, s, left, right):
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
