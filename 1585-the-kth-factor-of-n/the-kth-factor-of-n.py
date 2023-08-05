class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 1
        for num in range(1, n+1):
            if(n%num == 0):
                if(count == k):
                    return num
                count = count + 1
        return -1
            