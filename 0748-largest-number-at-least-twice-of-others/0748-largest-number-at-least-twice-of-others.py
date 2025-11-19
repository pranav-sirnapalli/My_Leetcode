class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        for i in nums:
            if (i*2) > max_val and i != max_val:
                return -1
        for i in range(len(nums)):
            if max_val == nums[i]:
                return i

        