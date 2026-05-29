class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        f = [0] * 26

        for i in range(len(s)):
            f[ord(s[i]) - ord('a')] += 1
            f[ord(t[i]) - ord('a')] -= 1
        
        for v in f:
            if (v != 0):
                return False
        return True