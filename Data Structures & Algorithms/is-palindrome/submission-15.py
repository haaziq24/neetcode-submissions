class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        var = ''

        for c in s:
            if c.isalnum(): 
                var += c.upper()

        return var == var[::-1]
