class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = {}

        for s in strs:
            sort = tuple(sorted(s))
            if sort not in count:
                count[sort] = []
            count[sort].append(s)

        return list(count.values())