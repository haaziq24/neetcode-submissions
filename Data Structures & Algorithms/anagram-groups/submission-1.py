class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}

        for s in strs:
            sort = ''.join(sorted(s))

            if sort not in count:
                count[sort] = [s]
            else:
                count[sort].append(s)

        return list(count.values())
        