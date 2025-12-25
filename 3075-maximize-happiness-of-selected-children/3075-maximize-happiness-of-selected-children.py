class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness.sort(reverse=True)
        for i in range(k):
            res += max(happiness[i]-i, 0)
        return res

        