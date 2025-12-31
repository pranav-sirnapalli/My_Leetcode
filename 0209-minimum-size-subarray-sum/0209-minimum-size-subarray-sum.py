class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        left = 0
        min_len = float("inf")
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                cur_len = right-left+1
                min_len = min(min_len, cur_len)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
                

                