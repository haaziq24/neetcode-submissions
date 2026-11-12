class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cand = [-1]
        curr_max = -1
        for num in arr[::-1]:
            if num < curr_max:
                cand.append(curr_max)
            else:
                cand.append(num)
            
            curr_max = max(curr_max, num)

        return cand[-2::-1]
        