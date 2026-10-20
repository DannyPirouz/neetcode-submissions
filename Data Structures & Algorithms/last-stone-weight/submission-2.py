class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x != y:
                newWeight = abs(x-y)
                heapq.heappush(maxHeap, -newWeight)
        
        if maxHeap:
            return -maxHeap[0]
        return 0

                
