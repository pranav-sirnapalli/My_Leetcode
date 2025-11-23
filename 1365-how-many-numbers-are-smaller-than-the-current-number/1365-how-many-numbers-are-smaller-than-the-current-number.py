class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        
        for i in range(length):
            count = 0
            val = nums[i]
            for cmp in nums:
                if cmp < val:
                    count += 1
            res.append(count)
        return res