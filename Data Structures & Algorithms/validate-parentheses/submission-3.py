class Solution:
    def isValid(self, s: str) -> bool:

        bracket = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c not in bracket:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != bracket[c]:
                        return False

        return not stack

