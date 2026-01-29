class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        found = set()
        for i in nums:
            if i in found:
                res.append(i)
            else:
                found.add(i)
        return res