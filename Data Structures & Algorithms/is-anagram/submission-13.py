class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_list = [0] * 26

        for c in s:
            f_list[ord(c)-97] += 1
        for c in t:
            f_list[ord(c)-97] -= 1
        
        return not any(f_list)