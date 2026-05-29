class Solution:
    def calculate_frequency_list(self, string: str) -> List[int]:
        f = [0] * 26
        for c in string:
            f[ord(c)-97] = f[ord(c)-97] + 1
        return f

    def isAnagram(self, s: str, t: str) -> bool:
        frequency_list = []
        a = self.calculate_frequency_list(s)
        b = self.calculate_frequency_list(t)
        return a == b