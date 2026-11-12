class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = {}
        count2 = {}

        for string1 in s:
            if string1 in count:
                count[string1] += 1
            else:
                count[string1] = 1

        for string2 in t:
            if string2 in count2:
                count2[string2] += 1
            else:
                count2[string2] = 1

        return count == count2        