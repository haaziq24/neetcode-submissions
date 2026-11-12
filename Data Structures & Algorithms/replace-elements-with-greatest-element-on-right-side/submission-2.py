class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            right_max = sorted(arr[i+1:])[-1]
            arr[i] = right_max
        arr[-1] = -1
        return arr
        