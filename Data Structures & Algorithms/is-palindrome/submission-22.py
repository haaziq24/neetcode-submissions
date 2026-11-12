class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        if len(s) == 1:
            return True

        # pass left and right pointers across eachother from start to end and end to start
        # skip alnum characters. If they are equal throughout then its a palindrome
        # any disagreement means its not a palindrome
        l = 0
        r = len(s) - 1
        while l < r:
            # skip alphanumerical characters
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # do they match?
            if s[l] != s[r]:
                return False
            # check next character
            l += 1
            r -= 1
        
        return True