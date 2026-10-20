class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0
        left = 0 
        right = len(heights) - 1
        
        while left < right:
            distance = right - left
            height = min(heights[left], heights[right])
            area = distance * height
            output = max(output, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return output