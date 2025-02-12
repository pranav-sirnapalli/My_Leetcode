class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur_sum = sum(nums)
        max_val = len(nums)

        tot_sum = 0
        for i in range(max_val+1):
            tot_sum = tot_sum + i
        
        return tot_sum - cur_sum