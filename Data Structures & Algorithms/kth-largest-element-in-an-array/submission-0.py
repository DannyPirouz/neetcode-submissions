class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        x = 0
        for _ in range(k):
            x = heapq.heappop(nums)
        
        return -x

