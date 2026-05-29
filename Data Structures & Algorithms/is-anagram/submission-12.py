class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f_map = defaultdict(int)

        for c in s:
            f_map[c] += 1
        for c in t:
            f_map[c] -= 1
        
        return not any(f_map.values())