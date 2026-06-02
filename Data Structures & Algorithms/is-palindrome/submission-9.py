class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum() or not s[r].isalnum():
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
                continue
            if s.lower()[l] != s.lower()[r]:
                return False
            l += 1
            r -= 1
        return True