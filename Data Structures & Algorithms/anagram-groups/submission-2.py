class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            rep = self.to_rep(s)
            m[rep].append(s)
        
        return list(m.values())

    def to_rep(self, string: str) -> tuple[str]:
        rep_arr = [0] * 26
        for char in string:
            rep_arr[ord(char) - 97] += 1
        return tuple(rep_arr)
