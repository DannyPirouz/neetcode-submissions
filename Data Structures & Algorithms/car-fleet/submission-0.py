class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[0] for i in range(len(position))]
        stack = []

        for i in range(len(position)):
            pair[i] = [position[i], speed[i]]

        pair = sorted(pair, reverse=True)

        for p, s in pair:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        
        return len(stack)