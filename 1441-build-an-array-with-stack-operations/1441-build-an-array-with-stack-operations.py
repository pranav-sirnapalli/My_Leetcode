class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 1

        while i <= n:
            if i in target:
                res.append("Push")
            elif i not in target and (i-1) != max(target):
                res.append("Push")
                res.append("Pop")
            else:
                break
            i += 1
        return res
        