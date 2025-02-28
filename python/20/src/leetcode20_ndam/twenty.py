#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.

import pdb

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in {'(','[','{'}:
                stack.append(char)
            elif len(stack) < 1:
                return False
            elif stack[-1] != matching[char]:
                return False
            else:
                stack.pop(-1)
        if len(stack) != 0: 
            return False 
        return True 


def main():
    sol = Solution()
    s = "(){}[]"
    print(sol.isValid(s))

if __name__ == "__main__":
    main()
