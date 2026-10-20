class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]

        if n <= 2:
            return fib[n]

        for _ in range(3, n+1):
            temp1 = fib[0]
            temp2 = fib[1]
            temp3 = fib[2]
            fib[0] = temp2
            fib[1] = temp3
            fib[2] = temp1 + temp2 + temp3
        return fib[2]
