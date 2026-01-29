class Solution:
    def trimMean(self, arr: List[int]) -> float:
        len_to_rem = int(0.05 * len(arr))
        arr.sort()
        i = len_to_rem
        j = len(arr) - len_to_rem

        tot_val = sum(arr[i:j])
        req_len = len(arr) - (2 * len_to_rem)
        return float(tot_val / req_len)
        