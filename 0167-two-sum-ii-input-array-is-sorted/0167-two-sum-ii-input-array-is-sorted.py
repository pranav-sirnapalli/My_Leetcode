class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #res = []
        for i in range(len(numbers)):
            if target - numbers[i] in numbers:
                if numbers.index(target-numbers[i]) == i:
                    return [i+1, numbers.index(target-numbers[i])+2]
                return [i+1, numbers.index(target-numbers[i])+1]