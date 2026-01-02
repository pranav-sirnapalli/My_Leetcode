class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        found = set()
        for i in nums:
            if i in found:
                return i
            else:
                found.add(i)