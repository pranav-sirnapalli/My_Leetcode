class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        len_n = len(nums)

        freq = {}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0 ) + 1
        
        if not freq:
            return -1
        max_value = max(freq.values())
        res = float("inf")

        for key, value in freq.items():
            if value == max_value:
                res = min(res, key)
        return res