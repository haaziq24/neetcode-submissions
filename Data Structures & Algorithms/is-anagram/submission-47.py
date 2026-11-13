class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count, count_two = {}, {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count_two[t[i]] = 1 + count_two.get(t[i], 0)

        return count == count_two