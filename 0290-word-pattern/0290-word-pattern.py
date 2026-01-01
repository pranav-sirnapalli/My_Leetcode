class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        #print(s_list)
        p_list = []
        for i in range(len(pattern)):
            p_list.append(pattern[i])
        #print(p_list)
        res = {}
        limit = max(len(p_list), len(s_list))
        for i in range(limit):
            if i > (len(p_list)-1):
                return False
            if p_list[i] not in res.keys():
                if s_list[i] in res.values():
                    return False
                res[p_list[i]] = s_list[i]
            else:
                if res[p_list[i]] != s_list[i]:
                    return False
        return True

        