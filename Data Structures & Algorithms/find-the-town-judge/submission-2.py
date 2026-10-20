class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        judge = -1

        for src, dst in trust:
            incoming[dst] += 1
            outgoing[src] += 1
        for i in incoming.keys():
            if incoming[i] == n-1:
                judge = i
        if outgoing[judge] != 0:
            return -1
        return judge
        
            
