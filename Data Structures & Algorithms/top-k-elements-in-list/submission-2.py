from _heapq import heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        heap = []

        for keyOne, _ in count.items():
            heapq.heappush(heap, (count[keyOne], keyOne))
        
        while len(heap) > k:
            heapq.heappop(heap)

        while len(heap):
            key, value = heapq.heappop(heap)
            result.append(value)
        return result