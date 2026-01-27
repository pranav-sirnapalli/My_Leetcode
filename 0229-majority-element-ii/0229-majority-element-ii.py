class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        res = []
        for key, value in freq.items():
            if value > num_len // 3:
                res.append(key)
        return res
