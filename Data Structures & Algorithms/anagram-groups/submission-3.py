class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = {}

        for s in strs:
            sort = ''.join(sorted(s))

            if sort in count:
                count[sort].append(s)
            else:
                count[sort] = [s]

        return list(count.values())