class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap = {"}" : "{" , ")" : "(" , "]" : "["}
        for c in s:
            if c in myMap:
                if stack and stack[-1] == myMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else: 
            return False
