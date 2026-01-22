class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            if ((ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122)) and \
             ((ord(s[j]) >= 65 and ord(s[j]) <= 90) or(ord(s[j]) >= 97 and ord(s[j]) <= 122)):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif not ((ord(s[i]) >= 65 and ord(s[i]) <= 90) or(ord(s[i]) >= 97 and ord(s[i]) <= 122)):
                i += 1
            else:
                j -= 1
        return "".join(s)