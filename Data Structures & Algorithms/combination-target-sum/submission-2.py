class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, path, total):
            if total == target:
                result.append(path[:])
                return
            
            if index >= len(nums) or total > target:
                return

            path.append(nums[index])
            backtrack(index, path, total + nums[index])
            path.pop()
            backtrack(index+1, path, total)
        
        backtrack(0, [], 0)
        return result


        