from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        right = {'(', '{', '['}
        left = {')', '}', ']'}
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for c in s:
            if c in right:
                stack.append(c)
            elif c in left:
                if stack:
                    top = stack[-1]
                else:
                    return False
                if mapping[top] == c:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return not stack

