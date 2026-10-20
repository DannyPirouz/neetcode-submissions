class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            head = s[left]
            tail = s[right]
            s[left] = tail
            s[right] = head
            left += 1
            right -= 1
        