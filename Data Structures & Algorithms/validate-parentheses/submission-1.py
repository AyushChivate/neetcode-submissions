class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(', '{', '['}
        closing = {')', '}', ']'}
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
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

