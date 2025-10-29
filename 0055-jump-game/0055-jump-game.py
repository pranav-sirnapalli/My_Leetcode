class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        last_val = len(nums)-1
        for i, val in enumerate(nums):
            if i > pos:
                return False
            pos = max(pos, i+val)
            if pos >= last_val:
                return True
        return True

        