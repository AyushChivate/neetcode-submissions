class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        repr_to_word = defaultdict(list)
        for word in strs:
            c_map = [0] * 26
            for char in word:
                c_map[ord(char) - ord('a')] += 1
            repr_to_word[tuple(c_map)].append(word)

        return list(repr_to_word.values())
