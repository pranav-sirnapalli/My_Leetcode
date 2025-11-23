class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_set = set(range(1, len(nums)+1))
        curr_set = set(nums)
        res = my_set.difference(curr_set)
        res_val = list(res)
        return res_val
