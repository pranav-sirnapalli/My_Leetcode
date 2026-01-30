class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_val = float("inf")
        arr.sort()
        i = 0
        j = 1
        while j < len(arr):
            min_val = min(min_val, arr[j]-arr[i])
            i += 1
            j += 1
       # print(min_val)
        res = []
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) == min_val:
                res.append([arr[i], arr[i+1]])
        return res           
        