
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(([j, i] for i, x in enumerate(nums) for j in range(i) if nums[j] + x == target), [])
