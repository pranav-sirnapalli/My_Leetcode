class Solution:
    def isThree(self, n: int) -> bool:
        div = 0
        for i in range(1, n+1):
            if(n % i == 0):
                div = div + 1
        if(div == 3):
            return True
        return False