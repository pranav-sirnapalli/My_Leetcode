class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        curSum = 0
        for n in nums:
            if(curSum < 0):
                curSum = 0
            curSum = curSum + n
            maxsum = max(maxsum, curSum)
        return maxsum
        