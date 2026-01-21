class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if(len(nums)) <= 2:
            return -1
        nums.sort()
        del nums[0]
        del nums[-1]
        return nums[0]