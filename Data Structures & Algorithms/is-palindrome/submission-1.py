class Solution:
    def isPalindrome(self, s: str) -> bool:
        startPos = 0
        endPos = len(s) - 1

        while startPos < endPos:
            if not s[startPos].isalnum():
                startPos += 1
                continue
            if not s[endPos].isalnum():
                endPos -= 1
                continue
            if s[startPos].lower() != s[endPos].lower():
                return False
            else:
                startPos += 1
                endPos -= 1
        return True