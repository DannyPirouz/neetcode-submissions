class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        output.append(asteroids[0])

        for i in range(1, len(asteroids)):
            if not (output and output[-1] >= 0 and asteroids[i] <= 0):
                output.append(asteroids[i])
                continue
            while (output and output[-1] >= 0 and asteroids[i] <= 0):
                if output[-1] + asteroids[i] == 0:
                    output.pop()
                    break
                if output[-1] + asteroids[i] > 0:
                    break
                if output[-1] + asteroids[i] < 0:
                    output.pop()
                    continue
            else:
                output.append(asteroids[i])
        return output

            