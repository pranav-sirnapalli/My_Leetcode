class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        all_elements = set()
        for i in nums:
            if i not in all_elements:
                all_elements.add(i)
            else:
                return True
        return False
        