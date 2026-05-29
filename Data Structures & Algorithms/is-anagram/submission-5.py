class Solution:
    def calculate_frequency_list(self, string: str) -> List[int]:
        f = [0] * 26
        for c in string:
            charOrd = ord(c)-97
            f[charOrd] = f[charOrd] + 1
        return f

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = self.calculate_frequency_list(s)
        b = self.calculate_frequency_list(t)
        return a == b