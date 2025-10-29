class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0

        for val in nums:
            tmp = max(n1+val, n2)
            n1 = n2
            n2 = tmp
        return n2