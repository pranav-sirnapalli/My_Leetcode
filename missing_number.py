class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # Finding the length of the array
        sum_tot = (n * (n+1)) / 2 # Getting the total sum of n elements
        sum_arr = 0
        for i in nums:
            sum_arr = sum_arr + i  # Getting sum of all elements in given array
        res = sum_tot - sum_arr # sum till n minus the sum of array will give the missing positive
        return int(res)