class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        total = 0

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if t == "+":
                    total = num1 + num2
                elif t == "-":
                    total = num2 - num1
                elif t == "*":
                    total = num1 * num2
                elif t == "/":
                    total = num2 / num1
                stack.append(int(total))
        return stack.pop()

