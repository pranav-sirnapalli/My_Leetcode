class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found = set()
        res = []
        for i in nums:
            if i in found:
                res.append(i)
                break
            found.add(i)
        
        max_val = max(nums)
        for i in range(1, max_val+1):
            if i not in nums:
                res.append(i)
        if len(res) == 1:
            res.append(max(nums)+1)
        return res