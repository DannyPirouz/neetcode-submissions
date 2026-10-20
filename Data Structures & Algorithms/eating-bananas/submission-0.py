class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        left = 1
        right = max(piles)
        tempRes = 0

        while left <= right:
            middle = (left + right) // 2
            for pile in piles:
                tempRes += math.ceil(float(pile) / middle)
            if tempRes <= h:
                right = middle - 1
                result = middle
            elif tempRes >= h:
                left = middle + 1
            tempRes = 0
        return result
