class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            val = i * i
            res.append(val)
        res.sort()
        return res