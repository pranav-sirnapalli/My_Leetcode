class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        length = len(nums)
        for i in range(length):
            if nums[i] == original:
                original = 2 * original
        return original
        