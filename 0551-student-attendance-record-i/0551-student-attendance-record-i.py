class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        length = len(s)
        for i in range(length):
            if s[i] == 'A':
                count += 1
        
        if count >= 2:
            return False
        count = 0
        for i in range(length):
            if s[i] == 'L' and s[i-1] != 'L':
                count = 1
            if s[i] == 'L' and s[i-1] == 'L':
                count += 1
            if count >= 3:
                return False
        return True
        