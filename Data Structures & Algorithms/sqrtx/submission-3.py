class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        result = 1
        if x == 0:
            return 0

        while left <= right:
            m = left + (right - left) // 2
            if m * m > x:
                right = m - 1
            elif m * m < x:
                result = m
                left = m + 1
            else:
                return m
        return result
