class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}
        for s in strs:
            si = tuple(sorted(s))
            if si not in count:
                count[si] = []
            count[si].append(s)
        return list(count.values())