class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        length = n
        i = 0
        while i < length:
            res.append(nums[i])
            i += 1
            res.append(nums[n])
            n += 1
        return res