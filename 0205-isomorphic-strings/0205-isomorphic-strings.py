class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]] = i
            
            if t[i] not in s2:
                s2[t[i]] = i
            
            if s1[s[i]] != s2[t[i]]:
                return False
        return True
        