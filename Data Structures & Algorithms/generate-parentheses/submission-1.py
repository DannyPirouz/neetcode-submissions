class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(opens, closed, stack):
            if opens == n and closed == n:
                result.append("".join(stack))
                return

            if opens < n:
                stack.append("(")
                backtrack(opens + 1, closed, stack)
                stack.pop()
            if closed < opens:
                stack.append(")")
                backtrack(opens, closed + 1, stack)
                stack.pop()

        backtrack(0, 0, [])
        return result