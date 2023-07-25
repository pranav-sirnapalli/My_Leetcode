class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_tot = (n * (n+1)) / 2
        sum_arr = 0
        for i in nums:
            sum_arr = sum_arr + i
        res = sum_tot - sum_arr
        return int(res)