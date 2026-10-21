class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    backtrack(path)
                    count[num] += 1
                    path.pop()

        backtrack([])
        return res
