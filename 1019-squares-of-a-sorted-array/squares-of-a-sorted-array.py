class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums