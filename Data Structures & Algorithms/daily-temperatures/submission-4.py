class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t  in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, index = stack.pop()
                days = i - index
                output[index] = days
                
            stack.append([t, i])
        return output
            