class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArray = nums[0]
        curr_sum = 0

        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + i
            maxArray = max(maxArray, curr_sum)
        return maxArray