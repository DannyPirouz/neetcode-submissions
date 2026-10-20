class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                first = stack[-1]
                second = stack[-2]
                result = first + second
                stack.append(result)
                continue
            if operations[i] == "D":
                top = stack[-1]
                result = top * 2
                stack.append(result)
                continue
            if operations[i] == "C":
                stack.pop()
                continue
            stack.append(int(operations[i]))
        total = sum(stack)
        return total