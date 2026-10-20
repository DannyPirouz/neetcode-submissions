class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                _, index = stack.pop()
                days = i - index
                output[index] = days
                
            stack.append([temperatures[i], i])
        return output
            