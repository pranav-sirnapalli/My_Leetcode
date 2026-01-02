class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        res = digits[0]
        for i in range(1, len(digits)):
            res = ((10 ** i) * digits[i]) + res
        
        res = res + 1

        net_res = 0
        val = []
        while res > 0:
            net_res = res % 10
            res = res // 10
            val.append(net_res)
        return val[::-1]


        