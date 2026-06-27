class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            win_len = r - l + 1
            counts[s[r]] += 1
            if win_len - max(counts.values()) <= k:
                max_len = max(max_len, win_len)
            else:
                counts[s[l]] -= 1
                l += 1
            r += 1
        return max_len



"""
Case 1.0: all unique
k=4
ABSDLKER

Case 2.0: first, out of range
k=4
ABSDLKEA

Case 2.1 first, inside range
k=4
ABSDLAER

Case 3.0: middle, out of range
k=3
ABSDLKES

Case 3.1: middle, inside range
k=3
ABSDLKSR

ABSDSKSR


k=1
AAABBJBB
BAAABJIEKBPLKB

"""