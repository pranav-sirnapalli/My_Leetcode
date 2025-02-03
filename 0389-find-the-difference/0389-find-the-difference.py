class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        all_char = {}

        for i in t:
            if i in all_char:
                all_char[i] += 1
            else:
                all_char[i] = 1
        
        for i in s:
            all_char[i] -= 1
        
        for i in all_char:
            if all_char[i] == 1:
                return i
        