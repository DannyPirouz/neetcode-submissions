class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = [0] * 3
        for bill in bills:
            if bill == 5:
                register[0] += 1
                continue
            if bill == 10:
                if register[0] < 1:
                    return False
                register[0] -= 1
                register[1] += 1
            if bill == 20:
                if register[1] >= 1 and register[0] >= 1:
                    register[0] -= 1
                    register[1] -= 1
                    register[2] += 1
                elif register[0] >= 3:
                    register[0] -= 3
                    register[2] += 1
                else:
                    return False
        return True
            

